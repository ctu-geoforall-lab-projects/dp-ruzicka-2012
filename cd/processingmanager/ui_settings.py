# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/camilo/Proyectos/qgis/python/plugins/processingmanager/settings.ui'
#
# Created: Thu Dec 15 23:34:28 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(480, 640)
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Processing Framework Settings", None, QtGui.QApplication.UnicodeUTF8))
        settingsDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settingsTabs = QtGui.QTabWidget(settingsDialog)
        self.settingsTabs.setTabPosition(QtGui.QTabWidget.West)
        self.settingsTabs.setObjectName(_fromUtf8("settingsTabs"))
        self.verticalLayout.addWidget(self.settingsTabs)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDialog)
        self.settingsTabs.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        pass

