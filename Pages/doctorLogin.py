
from PyQt5 import QtCore, QtWidgets
from Pages import helpPage, submitReport
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                             database='se315',
                                             user='root',
                                             password='')

cursor = connection.cursor()


class Ui_Dialog(object):

    def loginCheck(self):
        username = self.user_name.text()
        password = self.password.text()
        query = "SELECT * from doctors where username = %s AND password = %s"
        vals = (username, password)
        cursor.execute(query, (vals))
        result = cursor.fetchall()
        if(len(result) > 0):
            for row in result:
                self.name = row[3]
                self.surname = row[4]
                self.ID = row[0]
            self.pushButton.clicked.connect(self.openSubmitWindow)
        else:
            print("No User Found")

    def openHelpPage(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = helpPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSubmitWindow(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = submitReport.Ui_Dialog(self.name, self.surname, self.ID)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 486)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 251, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 100, 131, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 250, 91, 21))
        self.label_3.setObjectName("label_3")

        self.user_name = QtWidgets.QLineEdit(Dialog)
        self.user_name.setGeometry(QtCore.QRect(200, 240, 181, 31))
        self.user_name.setObjectName("textBrowser")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 290, 81, 31))
        self.label_4.setObjectName("label_4")

        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(200, 290, 181, 31))
        self.password.setObjectName("textBrowser_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 360, 75, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginCheck)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(160, 420, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.openHelpPage)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Doctor Login"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; font-style:italic; color:#34848d;\">BrightBorn</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#a21225;\">Doctor</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Username:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Password :</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.commandLinkButton.setText(_translate("Dialog", "Forgot Password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
