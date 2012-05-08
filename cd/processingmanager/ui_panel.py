# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/czenda/piskoviste/qgis_PF_cze/qgis/python/plugins/processingmanager/panel.ui'
#
# Created: Mon Mar  5 13:28:25 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dock(object):
    def setupUi(self, dock):
        dock.setObjectName(_fromUtf8("dock"))
        dock.resize(256, 308)
        dock.setFloating(False)
        self.contents = QtGui.QWidget()
        self.contents.setObjectName(_fromUtf8("contents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.filterBox = QtGui.QComboBox(self.contents)
        self.filterBox.setEditable(True)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.verticalLayout.addWidget(self.filterBox)
        self.moduleList = QModuleTreeView(self.contents)
        self.moduleList.setObjectName(_fromUtf8("moduleList"))
        self.verticalLayout.addWidget(self.moduleList)
        dock.setWidget(self.contents)

        self.retranslateUi(dock)
        QtCore.QMetaObject.connectSlotsByName(dock)

    def retranslateUi(self, dock):
        dock.setWindowTitle(QtGui.QApplication.translate("dock", "Processing Modules", None, QtGui.QApplication.UnicodeUTF8))

from gui import QModuleTreeView
