# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/czenda/piskoviste/qgis_PF_cze/qgis/python/plugins/processingmanager/savedialog.ui'
#
# Created: Thu Apr  5 16:11:39 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_savedialog(object):
    def setupUi(self, savedialog):
        savedialog.setObjectName(_fromUtf8("savedialog"))
        savedialog.resize(693, 516)
        self.verticalLayout = QtGui.QVBoxLayout(savedialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(savedialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaParameters = QtGui.QWidget()
        self.scrollAreaParameters.setGeometry(QtCore.QRect(0, 0, 673, 291))
        self.scrollAreaParameters.setObjectName(_fromUtf8("scrollAreaParameters"))
        self.formParameters = QtGui.QFormLayout(self.scrollAreaParameters)
        self.formParameters.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formParameters.setObjectName(_fromUtf8("formParameters"))
        self.scrollArea.setWidget(self.scrollAreaParameters)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelName = QtGui.QLabel(savedialog)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.lineEditName = QtGui.QLineEdit(savedialog)
        self.lineEditName.setText(_fromUtf8(""))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelTags = QtGui.QLabel(savedialog)
        self.labelTags.setObjectName(_fromUtf8("labelTags"))
        self.gridLayout.addWidget(self.labelTags, 1, 0, 1, 1)
        self.lineEditTags = QtGui.QLineEdit(savedialog)
        self.lineEditTags.setText(_fromUtf8(""))
        self.lineEditTags.setObjectName(_fromUtf8("lineEditTags"))
        self.gridLayout.addWidget(self.lineEditTags, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.description = QtGui.QPlainTextEdit(savedialog)
        self.description.setMaximumSize(QtCore.QSize(16777215, 100))
        self.description.setObjectName(_fromUtf8("description"))
        self.verticalLayout.addWidget(self.description)
        self.buttonBox = QtGui.QDialogButtonBox(savedialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(savedialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), savedialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), savedialog.reject)
        QtCore.QMetaObject.connectSlotsByName(savedialog)

    def retranslateUi(self, savedialog):
        savedialog.setWindowTitle(QtGui.QApplication.translate("savedialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("savedialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTags.setText(QtGui.QApplication.translate("savedialog", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setPlainText(QtGui.QApplication.translate("savedialog", "Description...", None, QtGui.QApplication.UnicodeUTF8))

