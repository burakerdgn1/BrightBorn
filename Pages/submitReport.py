# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from string import digits

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Pages import basicReport

connection = mysql.connector.connect(host='localhost',
                                     database='se315',
                                     user='root',
                                     password='')

cursor = connection.cursor()

hbbQuery = "SELECT  * FROM hbbmutant"
cftrQuery = "SELECT * FROM cftrmutant"
httQuery = "SELECT  * FROM httmutant"
oca2Query = "SELECT * FROM oca2mutant"
tp53Query = "SELECT * FROM tp53mutant"
pahQuery = "SELECT  * FROM  pahmutant"

class Ui_Dialog(object):
    def __init__(self, name, surname, ID):
        self.name = name
        self.surname = surname
        self.ID = str(ID)

    def pushButtonHandlerMan(self):
        self.getManGeneInfo()

    def getManGeneInfo(self):
        remove_digits = str.maketrans('', '', digits)
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        a = open(path, "r").read().replace(" ", "").translate(remove_digits).replace("\n", "")

        self.cftrMan = a[282662:471362]
        self.hbbMan = a[754024:755584]
        self.httMan = a[1038246:1207506]
        self.tp53Man = a[1490168:1509308]
        self.pahMan = a[1791970:1913470]
        self.oca2Man = a[1913470:2257870]

    def pushButtonHandlerWoman(self):
        self.getWomanGeneInfo()

    def getWomanGeneInfo(self):
        remove_digits = str.maketrans('', '', digits)
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        print(path)
        a = open(path, "r").read().replace(" ", "").translate(remove_digits).replace("\n", "")
        self.cftrWoman = a[282662:471362]
        self.hbbWoman = a[754024:755584]
        self.httWoman = a[1038246:1207506]
        self.tp53Woman = a[1490168:1509308]
        self.pahWoman = a[1791970:1913470]
        self.oca2Woman = a[1913470:2257870]

    def checkHealthStatus(self, hbb, cftr, oca, pah, htt, tp53, TC_ID):
            selectionQuery = "Select * FROM patients where id = 0"
            insertionHealthStatus = "UPDATE patients SET reshbb = %s, rescftr = %s, resoca2 = %s, respah = %s, reshtt = %s, resp53 = %s WHERE TC_ID = %s"

            cursor.execute(selectionQuery)
            HEALTHY_records = cursor.fetchall()

            for row in HEALTHY_records:
                HEALTHYhbb = row[1]
                HEALTHYcftr = row[2]
                HEALTHYoca = row[3]
                HEALTHYpah = row[4]
                HEALTHYhtt = row[5]
                HEALTHYtp53 = row[6]


            if HEALTHYhbb == hbb:
                hbbStatus = "healthy"
            else:
                hbbStatus = "Not Healthy"

            if HEALTHYcftr == cftr:
                cftrStatus = "healthy"
            else:
                cftrStatus = "Not Healthy"

            if HEALTHYoca == oca:
                oca2Status = "healthy"
            else:
                oca2Status = "Not Healthy"

            if HEALTHYpah == pah:
                pahStatus = "healthy"
            else:
                pahStatus = "Not Healthy"

            if HEALTHYhtt == htt:
                httStatus = "healthy"
            else:
                httStatus = "Not Healthy"

            if HEALTHYtp53 == tp53:
                tp53Status = "healthy"
            else:
                tp53Status = "Not Healthy"

            healthValues = (hbbStatus, cftrStatus, oca2Status, pahStatus, httStatus, tp53Status, TC_ID)
            cursor.execute(insertionHealthStatus, healthValues)
            connection.commit()

            self.checkMutantGensIfGenIsUnhealthy(hbb, cftr, oca, pah, htt, tp53, TC_ID)

    def checkMutantGensIfGenIsUnhealthy(self, hbb, cftr, oca, pah, htt, tp53, TC_ID):
        selectionQuery = "Select * FROM patients where TC_ID = %s"
        cursor.execute(selectionQuery, (TC_ID,))
        results = cursor.fetchall()

        for row in results:
            reshbb = row[7]
            rescftr = row[8]
            resoca2 = row[9]
            respah = row[10]
            reshtt = row[11]
            restp53 = row[12]


        if (restp53 == "Not Healthy"):
            cursor.execute(tp53Query)
            result = cursor.fetchall()
            for rows in result:
                TP53AGT_AGX = rows[1]
                TP53CGA_TGA = rows[2]
                TP53CGG_TGG = rows[3]
                TP53GAA_AAA = rows[4]
                TP53GAG_AAG = rows[5]
                TP53GAT_GAX = rows[6]
                TP53GCC_TGC = rows[7]
            if (TP53AGT_AGX == tp53):
                self.TP53Reason = "TP53AGT_AGX"
            elif (TP53CGA_TGA == tp53):
                self.TP53Reason = "TP53CGA_TGA"
            elif (TP53CGG_TGG == tp53):
                self.TP53Reason = "TP53CGG_TGG"
            elif (TP53GAA_AAA == tp53):
                self.TP53Reason = "TP53GAA_AAA"
            elif (TP53GAG_AAG == tp53):
                self.TP53Reason = "TP53GAG_AAG"
            elif (TP53GAT_GAX == tp53):
                self.TP53Reason = "TP53GAT_GAX"
            elif (TP53GCC_TGC == tp53):
                self.TP53Reason = "TP53GCC_TGC"
        else:
            self.TP53Reason = ""

        qq = "UPDATE patients SET tp53Diseases = %s WHERE TC_ID = %s"
        val = (self.TP53Reason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()

        if (respah == "Not Healthy"):
            cursor.execute(pahQuery)
            result = cursor.fetchall()
            for rows in result:
                PAH42AAA_GAA = rows[1]
                PAHATG_AGG = rows[2]
                PAHCAG_CAC = rows[3]
                PAHCGC_GGC = rows[4]
                PAHGAA_TAA = rows[5]
                PAHGCC_GAC = rows[6]
            if (PAH42AAA_GAA == pah):
                self.PAHReason = "PAH42AAA_GAA"
            elif (PAHATG_AGG == pah):
                self.PAHReason = "PAHATG_AGG"
            elif (PAHCAG_CAC == pah):
                self.PAHReason = "PAHCAG_CAC"
            elif (PAHCGC_GGC == pah):
                self.PAHReason = "PAHCGC_GGC"
            elif (PAHGAA_TAA == pah):
                self.PAHReason = "PAHGAA_TAA"
            elif (PAHGCC_GAC == pah):
                self.PAHReason = "PAHGCC_GAC"
        else:
            self.PAHReason = ""
        qq = "UPDATE patients SET pahDiseases = %s WHERE TC_ID = %s"
        val = (self.PAHReason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()


        if (reshtt == "Not Healthy"):
            cursor.execute(httQuery)
            result = cursor.fetchall()
            for rows in result:
                htt40 = rows[1]
                htt65 = rows[2]
                htt120 = rows[3]
                httACG_ATG = rows[4]
                httCCG_CTG = rows[5]
            if (htt40 == htt):
                self.HTTReason = "htt40"
            elif (htt65 == htt):
                self.HTTReason = "htt65"
            elif (htt120 == htt):
                self.HTTReason = "htt120"
            elif (httACG_ATG == htt):
                self.HTTReason = "httACG_ATG"
            elif (httCCG_CTG == htt):
                self.HTTReason = "httCCG_CTG"
        else:
            self.HTTReason = ""
        qq = "UPDATE patients SET httDiseases = %s WHERE TC_ID = %s"
        val = (self.HTTReason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()

        if (rescftr == "Not Healthy"):
            cursor.execute(cftrQuery)
            result = cursor.fetchall()
            for rows in result:
                cftr188 = rows[1]
                cftr1456 = rows[2]
                cftr1526 = rows[3]
                cftr1567 = rows[4]
                cftr1717 = rows[5]
                cftr220 = rows[6]
                cftr3808 = rows[7]
                cftr870 = rows[8]
                cftr3874 = rows[9]

            if (cftr188 == cftr):
                self.CFTRReason = "cftr188"
            elif (cftr1456 == cftr):
                self.CFTRReason = "cftr1456"
            elif (cftr1526 == cftr):
                self.CFTRReason = "cftr1526"
            elif (cftr1567 == cftr):
                self.CFTRReason = "cftr1567"
            elif (cftr1717 == cftr):
                self.CFTRReason = "cftr1717"
            elif (cftr220 == cftr):
                self.CFTRReason = "cftr220"
            elif (cftr3808 == cftr):
                self.CFTRReason = "cftr3808"
            elif (cftr870 == cftr):
                self.CFTRReason = "cftr870"
            elif (cftr3874 == cftr):
                self.CFTRReason = "cftr3874"
        else:
            self.CFTRReason = ""
        qq = "UPDATE patients SET cftrDiseases = %s WHERE TC_ID = %s"
        val = (self.CFTRReason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()

        if (resoca2 == "Not Healthy"):
            cursor.execute(oca2Query)
            result = cursor.fetchall()
            for rows in result:
                OCA2AGG_AGT = rows[0].replace("\n", "")
                OCA2CGG_TGG = rows[1].replace("\n", "")
                OCA2GGA_AGA = rows[2]
                OCA2GTG_TTG = rows[3].replace("\n", "")
                OCA2TGG_TAG = rows[4].replace("\n", "")
                OCA2TTT_TGT = rows[5].replace("\n", "")

            if (OCA2GGA_AGA == oca):
                self.OCA2Reason= "OCA2GGA_AGA"
            elif (OCA2AGG_AGT == oca):
                self.OCA2Reason= "OCA2AGG_AGT"
            elif (OCA2CGG_TGG == oca):
                self.OCA2Reason= "OCA2CGG_TGG"
            elif (OCA2GTG_TTG == oca):
                self.OCA2Reason= "OCA2GTG_TTG"
            elif (OCA2TGG_TAG == oca):
                self.OCA2Reason= "OCA2TGG_TAG"
            elif (OCA2TTT_TGT == oca):
                self.OCA2Reason= "OCA2TTT_TGT"
        else:
            self.OCA2Reason = ""
        qq = "UPDATE patients SET oca2Diseases = %s WHERE TC_ID = %s"
        val = (self.OCA2Reason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()


        if (reshbb == "Not Healthy"):
            cursor.execute(hbbQuery)
            result = cursor.fetchall()
            for rows in result:
                HBBATG_AAG = rows[1].replace("\n", "")
                HBBATG_ACG = rows[2].replace("\n", "")
                HBBATG_ATA = rows[3].replace("\n", "")
                HBBATG_ATC = rows[4].replace("\n", "")
                HBBGTG_ATG = rows[5].replace("\n", "")
                # DELTED ASK UGUR # HBBc328G = row[6]

            if (HBBATG_AAG == hbb):
                self.HBBReason= "HBBATG_AAG"
            elif (HBBATG_ACG == hbb):
                self.HBBReason= "HBBATG_ACG"
            elif (HBBATG_ATA == hbb):
                self.HBBReason= "HBBATG_ATA"
            elif (HBBATG_ATC == hbb):
                self.HBBReason= "HBBATG_ATC"
            elif (HBBGTG_ATG == hbb):
                self.HBBReason= "HBBGTG_ATG"
        else:
            self.HBBReason = ""
        qq = "UPDATE patients SET hbbDiseases = %s WHERE TC_ID = %s"
        val = (self.HBBReason, TC_ID)
        cursor.execute(qq, val)
        connection.commit()

    def saveDatabase(self):
        self.manID = self.patientIDMan.text()
        self.manName = self.fullNameMan.text()

        self.WomanID = self.patientIDWoman.text()
        self.WomanName = self.fullNameWoman.text()

        lastInsertedQuery = "Select * FROM patients order by id desc limit 1"

        query = "INSERT into patients(hbb, cftr, oca2, pah, htt, tp53, name, TC_ID, doctorID) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        valuesMan = (
        self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, self.manName, self.manID,
        self.ID)

        cursor.execute(query, valuesMan)
        connection.commit()

        cursor.execute(lastInsertedQuery)
        result = cursor.fetchall()
        for row in result:
            TC_ID = row[14]

        self.checkHealthStatus(self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, TC_ID)
        self.checkMutantGensIfGenIsUnhealthy(self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, TC_ID)

        valuesWoman = (self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, self.WomanName, self.WomanID, self.ID)
        cursor.execute(query, valuesWoman)
        connection.commit()

        cursor.execute(lastInsertedQuery)
        result = cursor.fetchall()
        for row in result:
            TC_ID = row[14]

        self.checkHealthStatus(self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, TC_ID)
        self.checkMutantGensIfGenIsUnhealthy(self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, TC_ID)

        self.baby()

    def xstr(self,s):
        if s is None:
            return " "
        return str(s)

    def baby(self):
        qMan = "Select * FROM patients where TC_ID = %s"
        qWoman = "Select * FROM patients where TC_ID = %s"
        qManValue = self.manID
        qWomanValue = self.WomanID

        cursor.execute(qMan, (qManValue,))
        res1 = cursor.fetchall()

        cursor.execute(qWoman, (qWomanValue,))
        res2 = cursor.fetchall()

        for row in res1:
            hbbM = row[7]
            cftrM = row[8]
            oca2M = row[9]
            pahM = row[10]
            httM = row[11]
            tp53M = row[12]

        for row in res2:
            hbbW = row[7]
            cftrW = row[8]
            oca2W = row[9]
            pahW = row[10]
            httW = row[11]
            tp53W = row[12]

        selectionQuery = "Select * FROM patients where TC_ID = %s"
        cursor.execute(selectionQuery, (qManValue,))
        results = cursor.fetchall()

        for row in results:
            hbbDiseaseMAN = row[17]
            cftrDiseaseMAN = row[19]
            ocaDisease2MAN = row[20]
            pahDiseaseMAN = row[18]
            httDiseaseMAN = row[21]
            tp53DiseaseMAN = row[22]

            hbbDiseaseMAN = self.xstr(hbbDiseaseMAN)
            cftrDiseaseMAN = self.xstr(cftrDiseaseMAN)
            ocaDisease2MAN = self.xstr(ocaDisease2MAN)
            pahDiseaseMAN = self.xstr(pahDiseaseMAN)
            httDiseaseMAN = self.xstr(httDiseaseMAN)
            tp53DiseaseMAN = self.xstr(tp53DiseaseMAN)

            hbbMAN = row[1]
            cftrMAN = row[2]
            oca2MAN = row[3]
            pahMAN = row[4]
            httMAN = row[5]
            tp53MAN = row[6]
            reportIDMan = row[0]

            TC_IDMan = row[14]

        selectionQuery = "Select * FROM patients where TC_ID = %s"
        cursor.execute(selectionQuery, (qWomanValue,))
        results = cursor.fetchall()


        for row in results:
            hbbDiseaseWOMAN = row[17]
            cftrDiseaseWOMAN = row[19]
            oca2DiseaseWOMAN = row[20]
            pahDiseaseWOMAN = row[18]
            httDiseaseWOMAN = row[21]
            tp53DiseaseWOMAN = row[22]

            hbbDiseaseWOMAN = self.xstr(hbbDiseaseWOMAN)
            cftrDiseaseWOMAN = self.xstr(cftrDiseaseWOMAN)
            oca2DiseaseWOMAN = self.xstr(oca2DiseaseWOMAN)
            pahDiseaseWOMAN = self.xstr(pahDiseaseWOMAN)
            httDiseaseWOMAN = self.xstr(httDiseaseWOMAN)
            tp53DiseaseWOMAN = self.xstr(tp53DiseaseWOMAN)

            hbbWOMAN = row[1]
            cftrWOMAN = row[2]
            oca2WOMAN = row[3]
            pahWOMAN = row[4]
            httWOMAN = row[5]
            tp53WOMAN = row[6]
            TC_IDWoman = row[14]
            reportIDWoman = row[0]
        versions = False

        cocukhbb2DieaseVersion1 = ""
        cocukoca2DieaseVersion1 = ""
        cocukcftr2DieaseVersion1 = ""
        cocukpah2DieaseVersion1 = ""
        cocukhtt2DieaseVersion1 = ""
        cocuktp532DieaseVersion1 = ""

        # hbb
        if (hbbW == "Not Healthy" and hbbM == "Not Healthy"):
            cocukhbb = "Not Healthy"
            if (hbbDiseaseMAN == hbbDiseaseWOMAN):
                cocukhbb2DieaseVersion1 = hbbDiseaseWOMAN
            else:
                cocukhbb2DieaseVersion1 = hbbDiseaseWOMAN + "" + hbbDiseaseMAN
                versions = True
        else:
            cocukhbb = "Healthy"

        # oca2
        if (oca2M == "healthy" and oca2W == "healthy"):
            cocukoca2 = "Healthy"
        else:
            cocukoca2 = "Not Healthy"
            if (oca2DiseaseWOMAN == ocaDisease2MAN):
                cocukoca2DieaseVersion1 = ocaDisease2MAN
            else:
                cocukoca2DieaseVersion1 = oca2DiseaseWOMAN + "" + ocaDisease2MAN
                versions = True

        # cftr
        if (cftrM == "healthy" and cftrW == "healthy"):
            cocukcftr = "Healthy"
        else:
            cocukcftr = "Not Healthy"
            if (cftrDiseaseMAN == cftrDiseaseWOMAN):
                cocukcftr2DieaseVersion1 = cftrDiseaseMAN
            else:
                cocukcftr2DieaseVersion1 = cftrDiseaseWOMAN + "" + cftrDiseaseMAN
                versions = True
        # pah
        if (pahW == "healthy" and pahM == "healthy"):
            cocukpah = "Healthy"
        else:
            cocukpah = "Not Healthy"
            if (pahDiseaseMAN == pahDiseaseWOMAN):
                cocukpah2DieaseVersion1 = pahDiseaseMAN
            else:
                cocukpah2DieaseVersion1 = pahDiseaseWOMAN + "" + pahDiseaseMAN
                versions = True
        # htt
        if (httW == "healthy" and httM == "healthy"):
            cocukhtt = "Healthy"
        else:
            cocukhtt = "Not Healthy"
            if (httDiseaseMAN == httDiseaseWOMAN):
                cocukhtt2DieaseVersion1 = httDiseaseMAN
            else:
                cocukhtt2DieaseVersion1 = httDiseaseWOMAN + "" + httDiseaseMAN
                versions = True
        # tp53
        if (tp53W == "healthy" and tp53M == "healthy"):
            cocuktp53 = "Healthy"
        else:
            cocuktp53 = "Not Healthy"
            if (tp53DiseaseMAN == tp53DiseaseWOMAN):
                cocuktp532DieaseVersion1 = tp53DiseaseWOMAN
            else:
                cocuktp532DieaseVersion1 = tp53DiseaseMAN + "" + tp53DiseaseWOMAN
                versions = True

        TC_IDWoman = str(TC_IDWoman)
        TC_IDMan = str(TC_IDMan)
        TC_IDCocuk = TC_IDMan + TC_IDWoman

        if (versions == True):
            childQ = """Insert Into patients(hbb, cftr, oca2, pah, htt, tp53,
             reshbb, rescftr, resoca2, respah, reshtt, resp53,name,
              TC_ID,doctorID, hbbDiseases, pahDiseases, cftrDiseases, oca2Diseases, httDiseases, tp53Diseases)
             Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            name = "kid"
            values = (hbbWOMAN, cftrWOMAN, oca2WOMAN, pahWOMAN, httWOMAN, tp53WOMAN,
                      cocukhbb, cocukcftr, cocukoca2, cocukpah, cocukhtt, cocuktp53,name, TC_IDCocuk, self.ID,
                      cocukhbb2DieaseVersion1, cocukpah2DieaseVersion1, cocukcftr2DieaseVersion1,
                      cocukoca2DieaseVersion1, cocukhtt2DieaseVersion1, cocuktp532DieaseVersion1)
            cursor.execute(childQ, values)
            connection.commit()


        if(versions == False):
            self.getP0Genes()
            print(self.hbb0)

            childQ = """Insert Into patients(hbb, cftr, oca2, pah, htt, tp53,
                         reshbb, rescftr, resoca2, respah, reshtt, resp53,name,
                          TC_ID,doctorID, hbbDiseases, pahDiseases, cftrDiseases, oca2Diseases, httDiseases, tp53Diseases)
                         Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            name = "kid"
            values = (self.hbb0, self.cftr0, self.oca20, self.pah0, self.htt0, self.tp530,
                      cocukhbb, cocukcftr, cocukoca2, cocukpah, cocukhtt, cocuktp53, name, TC_IDCocuk, self.ID,
                      cocukhbb2DieaseVersion1, cocukpah2DieaseVersion1, cocukcftr2DieaseVersion1,
                      cocukoca2DieaseVersion1, cocukhtt2DieaseVersion1, cocuktp532DieaseVersion1)
            cursor.execute(childQ, values)
            connection.commit()

        print("Man report ID: ", reportIDMan)
        print("Woman report ID: ", reportIDWoman)
        print("Baby reportID: ", reportIDWoman + 1)

    def getP0Genes(self):
        query = "Select * from patients where id = 0"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            self.hbb0 = row[1]
            self.cftr0 = row[2]
            self.oca20 = row[3]
            self.pah0 = row[4]
            self.htt0 = row[5]
            self.tp530 = row[6]

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, 'Single File',
                                               "C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/documents", '*.text')
        print('filePath ', filePath)
        fileHandle = open(filePath, 'r')
        lines = fileHandle.readlines()
        for line in lines:
            print(line)

    def openSayfa5(self):
        self.window = QtWidgets.QMainWindow()
        self.message = self.reportID.text()
        print(self.message)
        self.ui = basicReport.Ui_Dialog(self.message)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 532)

        ##

        self.fullNameMaleLabel = QtWidgets.QLabel(Dialog)
        self.fullNameMaleLabel.setGeometry(QtCore.QRect(203, 255, 81, 21))
        self.fullNameMaleLabel.setObjectName("fullNameMaleLabel")

        self.patientIDMaleLabel = QtWidgets.QLabel(Dialog)
        self.patientIDMaleLabel.setGeometry(QtCore.QRect(203, 315, 81, 21))
        self.patientIDMaleLabel.setObjectName("patientIDMaleLabel")

        self.fullNameFemaleLabel = QtWidgets.QLabel(Dialog)
        self.fullNameFemaleLabel.setGeometry(QtCore.QRect(432, 255, 81, 21))
        self.fullNameFemaleLabel.setObjectName("fullNameFemaleLabel")


        self.patientIDFemaleLabel = QtWidgets.QLabel(Dialog)
        self.patientIDFemaleLabel.setGeometry(QtCore.QRect(432, 315, 81, 21))
        self.patientIDFemaleLabel.setObjectName("patientIDFemaleLabel")

        self.reportIDLabel = QtWidgets.QLabel(Dialog)
        self.reportIDLabel.setGeometry(QtCore.QRect(220, 25, 141, 51))
        self.reportIDLabel.setObjectName("reportIDLabel")


        ##

        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(180, 150, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(170, 0, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.doctorID = QtWidgets.QTextEdit(Dialog)
        self.doctorID.setGeometry(QtCore.QRect(10, 230, 161, 31))
        self.doctorID.setObjectName("textEdit")

        self.doctorName = QtWidgets.QTextEdit(Dialog)
        self.doctorName.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.doctorName.setObjectName("textEdit_2")

        self.doctorSurname = QtWidgets.QTextEdit(Dialog)
        self.doctorSurname.setGeometry(QtCore.QRect(10, 370, 161, 31))
        self.doctorSurname.setObjectName("textEdit_3")

        self.radioButtonFemale = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFemale.setGeometry(QtCore.QRect(530, 200, 82, 17))
        self.radioButtonFemale.setObjectName("radioButton_2")

        self.fullNameMan = QtWidgets.QLineEdit(Dialog)
        self.fullNameMan.setGeometry(QtCore.QRect(280, 250, 104, 31))
        self.fullNameMan.setObjectName("textEdit_4")

        self.patientIDMan = QtWidgets.QLineEdit(Dialog)
        self.patientIDMan.setGeometry(QtCore.QRect(280, 310, 104, 31))
        self.patientIDMan.setObjectName("textEdit_5")

        self.saveButtonMan = QtWidgets.QPushButton(Dialog)
        self.saveButtonMan.setGeometry(QtCore.QRect(300, 380, 75, 61))
        self.saveButtonMan.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/submit.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButtonMan.setIcon(icon)
        self.saveButtonMan.setIconSize(QtCore.QSize(32, 32))
        self.saveButtonMan.setObjectName("pushButton_2")
        self.saveButtonMan.clicked.connect(self.pushButtonHandlerMan)

        self.saveButtonWoman = QtWidgets.QPushButton(Dialog)
        self.saveButtonWoman.setGeometry(QtCore.QRect(530, 380, 75, 61))
        self.saveButtonWoman.setText("")
        self.saveButtonWoman.setIcon(icon)
        self.saveButtonWoman.setIconSize(QtCore.QSize(32, 32))
        self.saveButtonWoman.setObjectName("pushButton_3")
        self.saveButtonWoman.clicked.connect(self.pushButtonHandlerWoman)

        self.radioButtonMale = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMale.setGeometry(QtCore.QRect(300, 200, 61, 20))
        self.radioButtonMale.setObjectName("radioButton")

        self.fullNameWoman = QtWidgets.QLineEdit(Dialog)
        self.fullNameWoman.setGeometry(QtCore.QRect(510, 250, 104, 31))
        self.fullNameWoman.setObjectName("textEdit_6")

        self.patientIDWoman = QtWidgets.QLineEdit(Dialog)
        self.patientIDWoman.setGeometry(QtCore.QRect(510, 310, 104, 31))
        self.patientIDWoman.setObjectName("textEdit_7")

        self.reportID = QtWidgets.QLineEdit(Dialog)
        self.reportID.setGeometry(QtCore.QRect(370, 20, 201, 61))
        self.reportID.setObjectName("textEdit_8")

        self.searchReportID = QtWidgets.QPushButton(Dialog)
        self.searchReportID.setGeometry(QtCore.QRect(430, 110, 75, 23))
        self.searchReportID.setObjectName("pushButton")
        self.searchReportID.clicked.connect(self.openSayfa5)

        self.submitData = QtWidgets.QPushButton(Dialog)
        self.submitData.setGeometry(QtCore.QRect(420, 470, 75, 23))
        self.submitData.setObjectName("pushButton_4")
        self.submitData.clicked.connect(self.saveDatabase)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.fullNameMaleLabel.raise_()
        self.patientIDMaleLabel.raise_()
        self.fullNameFemaleLabel.raise_()
        self.patientIDFemaleLabel.raise_()
        self.reportIDLabel.raise_()

        self.radioButtonMale.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.doctorID.raise_()
        self.doctorName.raise_()
        self.doctorSurname.raise_()
        self.radioButtonFemale.raise_()
        self.fullNameMan.raise_()
        self.saveButtonMan.raise_()
        self.patientIDMan.raise_()
        self.fullNameWoman.raise_()
        self.patientIDWoman.raise_()
        self.saveButtonWoman.raise_()
        self.reportID.raise_()
        self.searchReportID.raise_()
        self.submitData.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Submit Report"))
        self.doctorID.setHtml(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Doctor ID: " + self.ID + "</span></p></body></html>"))
        self.doctorName.setHtml(_translate("Dialog",
                                           "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Name: " + self.name + "</span></p></body></html>"))
        self.doctorSurname.setHtml(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Surname: " + self.surname + "</span></p></body></html>"))
        self.radioButtonFemale.setText(_translate("Dialog", "Female"))

        self.radioButtonMale.setText(_translate("Dialog", "Male"))

        self.searchReportID.setText(_translate("Dialog", "Check Report"))
        self.submitData.setText(_translate("Dialog", "Submit Data"))

        self.fullNameMaleLabel.setText(_translate("Dialog",
                                                  "<html><head/><body><p><span style=\" font-size:11pt;\">Full Name</span></p><p><br/></p></body></html>"))
        self.patientIDMaleLabel.setText(_translate("Dialog",
                                                   "<html><head/><body><p><span style=\" font-size:11pt;\">Patient ID</span></p><p><br/></p></body></html>"))
        self.fullNameFemaleLabel.setText(_translate("Dialog",
                                                    "<html><head/><body><p><span style=\" font-size:11pt;\">Full Name</span></p><p><br/></p></body></html>"))
        self.patientIDFemaleLabel.setText(_translate("Dialog",
                                                     "<html><head/><body><p><span style=\" font-size:11pt;\">Patient ID</span></p><p><br/></p></body></html>"))
        self.reportIDLabel.setText(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:20pt; color:#7d7d7d;\">Report ID</span></p></body></html>"))
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
