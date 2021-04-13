# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sayfa1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from Pages import patientLogin, helpPage, doctorLogin, information


class Ui_Dialog(object):
    def openPatientPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patientLogin.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWhatIsBrightBorn(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = information.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openHelpPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = helpPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = doctorLogin.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 558)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 40, 201, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 221, 61))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 240, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 330, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openPatientPage)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 410, 201, 31))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(530, 480, 191, 51))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.openWhatIsBrightBorn)
        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(100, 450, 61, 61))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setText("help")
        self.pushButton3.clicked.connect(self.openHelpPage)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Brightborn"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic; color:#448788;\">BrightBorn</span></p><p><span style=\" color:#448788;\"><br/></span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#448788;\">for your future...</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Doctor Login"))
        self.pushButton_2.setText(_translate("Dialog", "Patient Login"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Click  </span><a href=\"www.BrightBorn.com\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">button </span></a><span style=\" font-size:14pt;\"> for help...</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Dialog", "What is BrightBorn?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

