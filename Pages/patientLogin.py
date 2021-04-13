# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from Pages import basicReport


class Ui_Dialog(object):

    def openBasicReport(self):
        self.window = QtWidgets.QMainWindow()
        self.message = self.reportID.text()
        self.ui = basicReport.Ui_Dialog(self.message)
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(724, 544)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 20, 221, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 101, 81))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 300, 101, 21))
        self.label_3.setObjectName("label_3")

        self.reportID = QtWidgets.QLineEdit(Dialog)
        self.reportID.setGeometry(QtCore.QRect(320, 290, 201, 41))
        self.reportID.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 390, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openBasicReport)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Patient Login"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; color:#6a6967;\">BrightBorn</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#43a0a1;\">Patient</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#7e7e7e;\">Report ID :</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Check Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

