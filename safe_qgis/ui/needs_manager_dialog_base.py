# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'needs_manager_dialog_base.ui'
#
# Created: Mon Nov 17 13:05:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NeedsManagerDialogBase(object):
    def setupUi(self, NeedsManagerDialogBase):
        NeedsManagerDialogBase.setObjectName(_fromUtf8("NeedsManagerDialogBase"))
        NeedsManagerDialogBase.resize(750, 666)
        NeedsManagerDialogBase.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout_2 = QtGui.QGridLayout(NeedsManagerDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.profileLabel = QtGui.QLabel(NeedsManagerDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileLabel.sizePolicy().hasHeightForWidth())
        self.profileLabel.setSizePolicy(sizePolicy)
        self.profileLabel.setObjectName(_fromUtf8("profileLabel"))
        self.horizontalLayout_2.addWidget(self.profileLabel)
        self.profileComboBox = QtGui.QComboBox(NeedsManagerDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileComboBox.sizePolicy().hasHeightForWidth())
        self.profileComboBox.setSizePolicy(sizePolicy)
        self.profileComboBox.setObjectName(_fromUtf8("profileComboBox"))
        self.horizontalLayout_2.addWidget(self.profileComboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(NeedsManagerDialogBase)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(418, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.addButton = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMaximumSize(QtCore.QSize(32, 32))
        self.addButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/add_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setCheckable(False)
        self.addButton.setAutoDefault(True)
        self.addButton.setDefault(False)
        self.addButton.setFlat(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout_3.addWidget(self.addButton, 0, 3, 1, 1)
        self.removeButton = QtGui.QPushButton(self.page)
        self.removeButton.setMaximumSize(QtCore.QSize(32, 32))
        self.removeButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removeButton.setFont(font)
        self.removeButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/remove_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon1)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout_3.addWidget(self.removeButton, 0, 4, 1, 1)
        self.editButton = QtGui.QPushButton(self.page)
        self.editButton.setMaximumSize(QtCore.QSize(32, 32))
        self.editButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editButton.setFont(font)
        self.editButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/edit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout_3.addWidget(self.editButton, 0, 5, 1, 1)
        self.resourceListWidget = QtGui.QListWidget(self.page)
        self.resourceListWidget.setObjectName(_fromUtf8("resourceListWidget"))
        self.gridLayout_3.addWidget(self.resourceListWidget, 1, 0, 1, 6)
        self.provenanceLable = QtGui.QLabel(self.page)
        self.provenanceLable.setObjectName(_fromUtf8("provenanceLable"))
        self.gridLayout_3.addWidget(self.provenanceLable, 2, 0, 1, 1)
        self.provenanceLineEdit = QtGui.QLineEdit(self.page)
        self.provenanceLineEdit.setObjectName(_fromUtf8("provenanceLineEdit"))
        self.gridLayout_3.addWidget(self.provenanceLineEdit, 2, 1, 1, 5)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(521, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.discardButton = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.discardButton.sizePolicy().hasHeightForWidth())
        self.discardButton.setSizePolicy(sizePolicy)
        self.discardButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.discardButton.setFont(font)
        self.discardButton.setObjectName(_fromUtf8("discardButton"))
        self.gridLayout.addWidget(self.discardButton, 0, 2, 1, 1)
        self.acceptButton = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())
        self.acceptButton.setSizePolicy(sizePolicy)
        self.acceptButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.acceptButton.setFont(font)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.gridLayout.addWidget(self.acceptButton, 0, 3, 1, 1)
        self.resourceWidget = QtGui.QWidget(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resourceWidget.sizePolicy().hasHeightForWidth())
        self.resourceWidget.setSizePolicy(sizePolicy)
        self.resourceWidget.setObjectName(_fromUtf8("resourceWidget"))
        self.gridLayout.addWidget(self.resourceWidget, 1, 0, 1, 4)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.saveAsButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.saveAsButton.setObjectName(_fromUtf8("saveAsButton"))
        self.horizontalLayout.addWidget(self.saveAsButton)
        self.newButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.horizontalLayout.addWidget(self.newButton)
        self.importButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.horizontalLayout.addWidget(self.importButton)
        self.exportButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.closeButton = QtGui.QPushButton(NeedsManagerDialogBase)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(NeedsManagerDialogBase)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), NeedsManagerDialogBase.close)
        QtCore.QMetaObject.connectSlotsByName(NeedsManagerDialogBase)

    def retranslateUi(self, NeedsManagerDialogBase):
        NeedsManagerDialogBase.setWindowTitle(_translate("NeedsManagerDialogBase", "Minimum Needs Manager", None))
        self.profileLabel.setText(_translate("NeedsManagerDialogBase", "Profile", None))
        self.profileComboBox.setToolTip(_translate("NeedsManagerDialogBase", "Select a profile", None))
        self.label.setText(_translate("NeedsManagerDialogBase", "Resources for this profile", None))
        self.addButton.setToolTip(_translate("NeedsManagerDialogBase", "Add new resource", None))
        self.removeButton.setToolTip(_translate("NeedsManagerDialogBase", "Remove selected resource", None))
        self.editButton.setToolTip(_translate("NeedsManagerDialogBase", "Edit selected resource", None))
        self.provenanceLable.setText(_translate("NeedsManagerDialogBase", "Provenance", None))
        self.label_2.setText(_translate("NeedsManagerDialogBase", "Resource editor", None))
        self.discardButton.setToolTip(_translate("NeedsManagerDialogBase", "Discard and return", None))
        self.discardButton.setText(_translate("NeedsManagerDialogBase", "X", None))
        self.acceptButton.setToolTip(_translate("NeedsManagerDialogBase", "Accept and return", None))
        self.acceptButton.setText(_translate("NeedsManagerDialogBase", "✓", None))
        self.saveButton.setText(_translate("NeedsManagerDialogBase", "Save", None))
        self.saveAsButton.setText(_translate("NeedsManagerDialogBase", "Save As ...", None))
        self.newButton.setText(_translate("NeedsManagerDialogBase", "New...", None))
        self.importButton.setText(_translate("NeedsManagerDialogBase", "Import ...", None))
        self.exportButton.setText(_translate("NeedsManagerDialogBase", "Export ...", None))
        self.closeButton.setText(_translate("NeedsManagerDialogBase", "Close", None))

import resources_rc