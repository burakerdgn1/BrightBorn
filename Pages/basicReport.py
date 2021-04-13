# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from PyQt5 import QtCore, QtWidgets

from Pages import complexReport

connection = mysql.connector.connect(host='localhost',
                                     database='se315',
                                     user='root',
                                     password='')

cursor = connection.cursor()


class Ui_Dialog(object):
    def __init__(self, message):
        self.ID = message
        print("ID:", self.ID)
        query = "Select * FROM patients WHERE id = %s"
        cursor.execute(query, (self.ID,))
        result = cursor.fetchall()
        for row in result:
            self.reshbb = "HBB status: " + row[7] + "\n"
            self.rescftr = "CFTR status: " + row[8] + "\n"
            self.resoca2 = "OCA2 status: " + row[9] + "\n"
            self.respah = "PAH status: " + row[10] + "\n"
            self.reshtt = "HTT status: " + row[11] + "\n"
            self.resp53 = "P53 status: " + row[12] + "\n"


            self.hbbDiseases = "HBB Diseases: " + row[17] + "\n"
            self.pahDiseases = "Pah Diseases: " + row[18] + "\n"
            self.cftrDiseases = "CFTR Diseases: " + row[19] + "\n"
            self.oca2Diseases = "OCA2 Diseases: " + row[20] + "\n"
            self.httDiseases = "HTT Diseases: " + row[21] + "\n"
            self.tp53Diseases = "TP53 Diseases: " + row[22] + "\n"

            self.name = "Full Name: " + row[13] + "\n"



        self.values = self.reshbb + self.rescftr + self.resoca2 + self.respah + self.reshtt + self.resp53

        self.diseases = self.hbbDiseases + self.pahDiseases + self.cftrDiseases + self.oca2Diseases + self.httDiseases + self.tp53Diseases

        self.information = self.name

    def complexReport(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = complexReport.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(706, 512)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 241, 51))
        self.label.setObjectName("label")
        self.showHealthStatus = QtWidgets.QTextBrowser(Dialog)
        self.showHealthStatus.setGeometry(QtCore.QRect(40, 110, 211, 151))
        self.showHealthStatus.setObjectName("textBrowser_2")
        self.showHealthStatus.setText(self.values)


        self.ShowDiseasesNames = QtWidgets.QTextBrowser(Dialog)
        self.ShowDiseasesNames.setGeometry(QtCore.QRect(310, 110, 211, 151))
        self.ShowDiseasesNames.setObjectName("textBrowser_3")
        self.ShowDiseasesNames.setText(self.diseases)


        self.generalInformation = QtWidgets.QTextBrowser(Dialog)
        self.generalInformation.setGeometry(QtCore.QRect(40, 290, 211, 151))
        self.generalInformation.setObjectName("textBrowser_4")
        self.generalInformation.setText(self.information)

        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 290, 211, 151))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(500, 450, 201, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.complexReport)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(550, 20, 131, 151))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Report"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:18pt; color:#5d5d5d;\">Report ID : "+self.ID+"</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Dialog", "Detailed Report"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
