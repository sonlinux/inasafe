# coding=utf-8

"""Aggregate the aggregate hazard to the analysis layer."""

from numbers import Number

from PyQt4.QtCore import QPyNullVariant
from qgis.core import QGis, QgsFeatureRequest, QgsFeature

from safe.definitions.utilities import definition
from safe.definitions.fields import (
    aggregation_id_field,
    aggregation_name_field,
    hazard_id_field,
    hazard_class_field,
    exposure_type_field,
    total_affected_field,
    total_not_affected_field,
    total_not_exposed_field,
    total_field,
    affected_field,
    hazard_count_field,
    exposure_count_field,
    exposure_class_field,
    summarizer_fields,
    affected_summarizer_fields
)
from safe.definitions.processing_steps import (
    summary_4_exposure_summary_table_steps)
from safe.definitions.post_processors import post_processor_affected_function
from safe.definitions.layer_purposes import \
    layer_purpose_exposure_summary_table
from safe.definitions.hazard_classifications import not_exposed_class
from safe.gis.vector.tools import (
    create_field_from_definition,
    read_dynamic_inasafe_field,
    create_memory_layer)
from safe.gis.sanity_check import check_layer
from safe.gis.vector.summary_tools import (
    check_inputs, create_absolute_values_structure)
from safe.utilities.gis import qgis_version
from safe.utilities.profiling import profile
from safe.utilities.pivot_table import FlatTable

__copyright__ = "Copyright 2016, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


@profile
def exposure_summary_table(
        aggregate_hazard, exposure_summary=None, callback=None):
    """Compute the summary from the aggregate hazard to analysis.

    Source layer :
    | haz_id | haz_class | aggr_id | aggr_name | exposure_count |

    Output layer :
    | exp_type | count_hazard_class | total |

    :param aggregate_hazard: The layer to aggregate vector layer.
    :type aggregate_hazard: QgsVectorLayer

    :param exposure_summary: The layer impact layer.
    :type exposure_summary: QgsVectorLayer

    :param callback: A function to all to indicate progress. The function
        should accept params 'current' (int), 'maximum' (int) and 'step' (str).
        Defaults to None.
    :type callback: function

    :return: The new tabular table, without geometry.
    :rtype: QgsVectorLayer

    .. versionadded:: 4.0
    """
    output_layer_name = summary_4_exposure_summary_table_steps[
        'output_layer_name']
    processing_step = summary_4_exposure_summary_table_steps['step_name']

    source_fields = aggregate_hazard.keywords['inasafe_fields']

    source_compulsory_fields = [
        aggregation_id_field,
        aggregation_name_field,
        hazard_id_field,
        hazard_class_field,
        affected_field,
        total_field
    ]
    check_inputs(source_compulsory_fields, source_fields)

    absolute_values = create_absolute_values_structure(
        aggregate_hazard, ['all'])

    hazard_class = source_fields[hazard_class_field['key']]
    hazard_class_index = aggregate_hazard.fieldNameIndex(hazard_class)
    unique_hazard = aggregate_hazard.uniqueValues(hazard_class_index)

    unique_exposure = read_dynamic_inasafe_field(
        source_fields, exposure_count_field)

    flat_table = FlatTable('hazard_class', 'exposure_class')

    request = QgsFeatureRequest()
    request.setFlags(QgsFeatureRequest.NoGeometry)
    for area in aggregate_hazard.getFeatures():
        hazard_value = area[hazard_class_index]
        for exposure in unique_exposure:
            key_name = exposure_count_field['key'] % exposure
            field_name = source_fields[key_name]
            exposure_count = area[field_name]
            if not exposure_count or isinstance(
                    exposure_count, QPyNullVariant):
                exposure_count = 0

            flat_table.add_value(
                exposure_count,
                hazard_class=hazard_value,
                exposure_class=exposure
            )

        # We summarize every absolute values.
        for field, field_definition in absolute_values.iteritems():
            value = area[field]
            if not value or isinstance(value, QPyNullVariant):
                value = 0
            field_definition[0].add_value(
                value,
                all='all'
            )

    tabular = create_memory_layer(output_layer_name, QGis.NoGeometry)
    tabular.startEditing()

    field = create_field_from_definition(exposure_type_field)
    tabular.addAttribute(field)
    tabular.keywords['inasafe_fields'][exposure_type_field['key']] = (
        exposure_type_field['field_name'])

    hazard_keywords = aggregate_hazard.keywords['hazard_keywords']
    classification = hazard_keywords['classification']

    hazard_affected = {}
    for hazard_class in unique_hazard:
        if not hazard_class or isinstance(hazard_class, QPyNullVariant):
            hazard_class = 'NULL'
        field = create_field_from_definition(hazard_count_field, hazard_class)
        tabular.addAttribute(field)
        key = hazard_count_field['key'] % hazard_class
        value = hazard_count_field['field_name'] % hazard_class
        tabular.keywords['inasafe_fields'][key] = value

        hazard_affected[hazard_class] = post_processor_affected_function(
            classification=classification, hazard_class=hazard_class)

    field = create_field_from_definition(total_affected_field)
    tabular.addAttribute(field)
    tabular.keywords['inasafe_fields'][total_affected_field['key']] = (
        total_affected_field['field_name'])

    # essentially have the same value as NULL_hazard_count
    # but with this, make sure that it exists in layer so it can be used for
    # reporting, and can be referenced to fields.py to take the label.
    field = create_field_from_definition(total_not_affected_field)
    tabular.addAttribute(field)
    tabular.keywords['inasafe_fields'][total_not_affected_field['key']] = (
        total_not_affected_field['field_name'])

    field = create_field_from_definition(total_not_exposed_field)
    tabular.addAttribute(field)
    tabular.keywords['inasafe_fields'][total_not_exposed_field['key']] = (
        total_not_exposed_field['field_name'])

    field = create_field_from_definition(total_field)
    tabular.addAttribute(field)
    tabular.keywords['inasafe_fields'][total_field['key']] = (
        total_field['field_name'])

    summarization_dicts = {}
    if exposure_summary:
        summarization_dicts = summarize_result(exposure_summary, callback)

    sorted_keys = sorted(summarization_dicts.keys())

    for key in sorted_keys:
        affected_summarizer_field = affected_summarizer_fields[key]
        field = create_field_from_definition(affected_summarizer_field)
        tabular.addAttribute(field)
        tabular.keywords['inasafe_fields'][
            affected_summarizer_field['key']] = (
            affected_summarizer_field['field_name'])

    # For each absolute values
    for absolute_field in absolute_values.iterkeys():
        field_definition = definition(absolute_values[absolute_field][1])
        field = create_field_from_definition(field_definition)
        tabular.addAttribute(field)
        key = field_definition['key']
        value = field_definition['field_name']
        tabular.keywords['inasafe_fields'][key] = value

    for exposure_type in unique_exposure:
        feature = QgsFeature()
        attributes = [exposure_type]
        total_affected = 0
        total_not_affected = 0
        total_not_exposed = 0
        total = 0
        for hazard_class in unique_hazard:
            if not hazard_class or isinstance(hazard_class, QPyNullVariant):
                hazard_class = 'NULL'
            value = flat_table.get_value(
                hazard_class=hazard_class,
                exposure_class=exposure_type
            )
            attributes.append(value)

            if hazard_affected[hazard_class] == not_exposed_class['key']:
                total_not_exposed += value
            elif hazard_affected[hazard_class]:
                total_affected += value
            else:
                total_not_affected += value

            total += value

        attributes.append(total_affected)
        attributes.append(total_not_affected)
        attributes.append(total_not_exposed)
        attributes.append(total)

        if summarization_dicts:
            for key in sorted_keys:
                attributes.append(summarization_dicts[key].get(
                    exposure_type, 0))

        for i, field in enumerate(absolute_values.itervalues()):
            value = field[0].get_value(
                all='all'
            )
            attributes.append(value)

        feature.setAttributes(attributes)
        tabular.addFeature(feature)

        # Sanity check ± 1 to the result. Disabled for now as it seems ± 1 is
        # not enough. ET 13/02/17
        # total_computed = (
        #     total_affected + total_not_affected + total_not_exposed)
        # if not -1 < (total_computed - total) < 1:
        #     raise ComputationError

    tabular.commitChanges()

    tabular.keywords['title'] = layer_purpose_exposure_summary_table['name']
    if qgis_version() >= 21800:
        tabular.setName(tabular.keywords['title'])
    else:
        tabular.setLayerName(tabular.keywords['title'])
    tabular.keywords['layer_purpose'] = layer_purpose_exposure_summary_table[
        'key']

    check_layer(tabular, has_geometry=False)
    return tabular


@profile
def summarize_result(exposure_summary, callback=None):
    """Extract result based on summarizer field value and sum by exposure type.

    :param exposure_summary: The layer impact layer.
    :type exposure_summary: QgsVectorLayer

    :param callback: A function to all to indicate progress. The function
        should accept params 'current' (int), 'maximum' (int) and 'step' (str).
        Defaults to None.
    :type callback: function

    :return: Dictionary of attributes per exposure per summarizer field.
    :rtype: dict

    .. versionadded:: 4.2
    """
    summarization_dicts = {}
    summarizer_flags = {}

    for summarizer_field in summarizer_fields:
        if exposure_summary.fieldNameIndex(
                summarizer_field['field_name']) == -1:
            summarizer_flags[summarizer_field['key']] = False
        else:
            summarizer_flags[summarizer_field['key']] = True
            summarization_dicts[summarizer_field['key']] = {}

    for feature in exposure_summary.getFeatures():
        is_affected = feature[affected_field['field_name']]
        exposure_class_name = feature[exposure_class_field['field_name']]
        for summarizer_field in summarizer_fields:
            flag = summarizer_flags[summarizer_field['key']]
            if not flag:
                continue
            if is_affected:
                if exposure_class_name not in summarization_dicts[
                    summarizer_field['key']]:
                    summarization_dicts[summarizer_field['key']][
                        exposure_class_name] = 0
                value = feature[summarizer_field['field_name']]
                if isinstance(value, Number):
                    summarization_dicts[summarizer_field['key']][
                        exposure_class_name] += value

    return summarization_dicts
