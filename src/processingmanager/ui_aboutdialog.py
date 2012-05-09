# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/camilo/Proyectos/qgis/python/plugins/processingmanager/aboutdialog.ui'
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(518, 390)
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(aboutDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(aboutDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.aboutTabs = QtGui.QTabWidget(aboutDialog)
        self.aboutTabs.setTabPosition(QtGui.QTabWidget.South)
        self.aboutTabs.setObjectName(_fromUtf8("aboutTabs"))
        self.mainTab = QtGui.QWidget()
        self.mainTab.setObjectName(_fromUtf8("mainTab"))
        self.layoutWidget = QtGui.QWidget(self.mainTab)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 11, 471, 291))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.tabLayout = QtGui.QGridLayout(self.layoutWidget)
        self.tabLayout.setMargin(0)
        self.tabLayout.setObjectName(_fromUtf8("tabLayout"))
        self.logo = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(64, 64))
        self.logo.setMaximumSize(QtCore.QSize(64, 64))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/64")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.tabLayout.addWidget(self.logo, 0, 0, 2, 1)
        self.title = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setText(QtGui.QApplication.translate("aboutDialog", "QGIS Processing Framework", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setObjectName(_fromUtf8("title"))
        self.tabLayout.addWidget(self.title, 0, 1, 1, 1)
        self.description = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setText(QtGui.QApplication.translate("aboutDialog", "Core Framework, Manager & Saga Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.tabLayout.addWidget(self.description, 1, 1, 1, 1)
        self.txt = QtGui.QTextBrowser(self.layoutWidget)
        self.txt.setHtml(QtGui.QApplication.translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">The </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-style:italic;\">QGIS Processing Framework, </span><span style=\" font-family:\'Sans\'; font-size:10pt;\">its </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-style:italic;\">Manager Plugin</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> and the </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-style:italic;\">QGIS to SAGA Interface</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> are being developed by Camilo Polymeris for Quantum GIS.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Contributions by Julien Malik.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Many thanks to Paolo Cavallini &amp; Giuseppe Sucamelli at </span><a href=\"www.faunalia.it\"><span style=\" text-decoration: underline; color:#0000ff;\">Faunalia</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\">, Volker Wichmann, Martin Dobias and the </span><a href=\"www.qgis.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Quantum GIS</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\"> developers for their assistance.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Funding provided by Google through their </span><a href=\"www.google-melange.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Summer of Code</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\"> 2011 programme for open source software development.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">For support, contact </span><a href=\"mailto:cpolymeris@gmail.com\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">cpolymeris@gmail.com</span></a>, or visit <a href=\"http://polymeris.github.com/qgis/\"><span style=\" text-decoration: underline; color:#0000ff;\">the project\'s webpage</span></a>.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.txt.setOpenExternalLinks(True)
        self.txt.setObjectName(_fromUtf8("txt"))
        self.tabLayout.addWidget(self.txt, 2, 0, 1, 2)
        self.aboutTabs.addTab(self.mainTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.aboutTabs, 0, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), aboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        self.aboutTabs.setTabText(self.aboutTabs.indexOf(self.mainTab), QtGui.QApplication.translate("aboutDialog", "Processing Framework", None, QtGui.QApplication.UnicodeUTF8))

import processing_rc
