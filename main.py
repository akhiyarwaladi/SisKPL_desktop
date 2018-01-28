# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'landCover.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import makeModel as mm
import predictCl as pc


class Ui_Form(QtWidgets.QWidget):

    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        #self._dialog = None
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 627)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 811, 211))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_dataSample = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_dataSample.setGeometry(QtCore.QRect(400, 50, 93, 28))
        self.pushButton_dataSample.setObjectName("pushButton_dataSample")
        self.label_outputModel = QtWidgets.QLabel(self.groupBox)
        self.label_outputModel.setGeometry(QtCore.QRect(10, 110, 181, 16))
        self.label_outputModel.setObjectName("label_outputModel")
        self.label_dataSample = QtWidgets.QLabel(self.groupBox)
        self.label_dataSample.setGeometry(QtCore.QRect(10, 30, 251, 16))
        self.label_dataSample.setObjectName("label_dataSample")
        self.textEdit_dataSample = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_dataSample.setGeometry(QtCore.QRect(10, 50, 381, 41))
        self.textEdit_dataSample.setObjectName("textEdit_dataSample")
        self.textEdit_outputModel = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_outputModel.setGeometry(QtCore.QRect(10, 130, 381, 41))
        self.textEdit_outputModel.setObjectName("textEdit_outputModel")
        self.checkBox_buatModel = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_buatModel.setGeometry(QtCore.QRect(580, 30, 161, 20))
        self.checkBox_buatModel.setObjectName("checkBox_buatModel")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(530, 80, 55, 16))
        self.label.setObjectName("label")
        self.label_akurasi = QtWidgets.QLabel(self.groupBox)
        self.label_akurasi.setGeometry(QtCore.QRect(520, 110, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_akurasi.setFont(font)
        self.label_akurasi.setObjectName("label_akurasi")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 260, 811, 271))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_dataBaru = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_dataBaru.setGeometry(QtCore.QRect(10, 140, 381, 41))
        self.textEdit_dataBaru.setObjectName("textEdit_dataBaru")
        self.label_dataBaru = QtWidgets.QLabel(self.groupBox_2)
        self.label_dataBaru.setGeometry(QtCore.QRect(10, 120, 141, 16))
        self.label_dataBaru.setObjectName("label_dataBaru")
        self.label_dataKlasifikasi = QtWidgets.QLabel(self.groupBox_2)
        self.label_dataKlasifikasi.setGeometry(QtCore.QRect(10, 200, 141, 16))
        self.label_dataKlasifikasi.setObjectName("label_dataKlasifikasi")
        self.textEdit_dataKlasifikasi = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_dataKlasifikasi.setGeometry(QtCore.QRect(10, 220, 381, 41))
        self.textEdit_dataKlasifikasi.setObjectName("textEdit_dataKlasifikasi")
        self.pushButton_objekModel = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_objekModel.setGeometry(QtCore.QRect(400, 60, 93, 28))
        self.pushButton_objekModel.setObjectName("pushButton_objekModel")
        self.textEdit_objekModel = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_objekModel.setGeometry(QtCore.QRect(10, 60, 381, 41))
        self.textEdit_objekModel.setObjectName("textEdit_objekModel")
        self.label_objekModel = QtWidgets.QLabel(self.groupBox_2)
        self.label_objekModel.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.label_objekModel.setObjectName("label_objekModel")
        self.pushButton_dataBaru = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_dataBaru.setGeometry(QtCore.QRect(400, 140, 93, 28))
        self.pushButton_dataBaru.setObjectName("pushButton_dataBaru")
        self.checkBox_prediksiBaru = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_prediksiBaru.setGeometry(QtCore.QRect(580, 30, 201, 20))
        self.checkBox_prediksiBaru.setObjectName("checkBox_prediksiBaru")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 560, 121, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.checkBox_buatModel.setEnabled (True)
        self.checkBox_prediksiBaru.setEnabled (True)

        self.textEdit_dataSample.setEnabled(False)
        self.pushButton_dataSample.setEnabled(False)
        self.textEdit_outputModel.setEnabled(False)
        self.textEdit_dataBaru.setEnabled(False)
        self.pushButton_dataBaru.setEnabled(False)
        self.textEdit_objekModel.setEnabled(False)
        self.pushButton_objekModel.setEnabled(False)
        self.textEdit_dataKlasifikasi.setEnabled(False)

        self.checkBox_buatModel.toggled.connect(self.checkBox_toggled)
        self.checkBox_prediksiBaru.toggled.connect(self.checkBox_toggled)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Otomatisasi Klasifikasi Tutupan Lahan"))
        self.groupBox.setTitle(_translate("Form", "Buat Model"))
        self.pushButton_dataSample.setText(_translate("Form", "Browse"))
        self.label_outputModel.setText(_translate("Form", "Output Model.pkl"))
        self.label_dataSample.setText(_translate("Form", "Data sample (.csv)"))
        self.textEdit_dataSample.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7d7b7d;\">pathSample</span></p></body></html>"))
        self.textEdit_outputModel.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7d7b7d;\">pathOutputModel</span></p></body></html>"))
        self.checkBox_buatModel.setText(_translate("Form", "Buat model baru"))
        self.label.setText(_translate("Form", "Akurasi:"))
        self.label_akurasi.setText(_translate("Form", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Form", "Prediksi menggunakan model"))
        self.textEdit_dataBaru.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7d7b7d;\">pathDataBaru</span></p></body></html>"))
        self.label_dataBaru.setText(_translate("Form", "Data Baru (.tiff)"))
        self.label_dataKlasifikasi.setText(_translate("Form", "Data terklasifikasi (.tiff)"))
        self.textEdit_dataKlasifikasi.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7d7b7d;\">pathDataKlasifikasi</span></p></body></html>"))
        self.pushButton_objekModel.setText(_translate("Form", "Browse"))
        self.textEdit_objekModel.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7d7b7d;\">pathObjekModel</span></p></body></html>"))
        self.label_objekModel.setText(_translate("Form", "Objek Model (.pkl)"))
        self.pushButton_dataBaru.setText(_translate("Form", "Browse"))
        self.checkBox_prediksiBaru.setText(_translate("Form", "Sudah punya model"))
        self.pushButton.setText(_translate("Form", "Proses data"))

        self.pushButton_dataSample.clicked.connect(self.openDataSample)
        self.pushButton_objekModel.clicked.connect(self.openObjekModel)
        self.pushButton_dataBaru.clicked.connect(self.openDataBaru)

        self.pushButton.clicked.connect(self.executeCode)

    def openDataSample(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        self.textEdit_dataSample.setText(fileName)
        self.textEdit_outputModel.setText(os.path.dirname(fileName) + "/" + os.path.splitext(os.path.basename(fileName))[0] + "_decisionTree.pkl")
        #print(fileName)

    def openObjekModel(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        self.textEdit_objekModel.setText(fileName)

    def openDataBaru(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textEdit_dataBaru.setText(fileName)
        self.textEdit_dataKlasifikasi.setText(fileName + "/" + os.path.basename(fileName) + "_class.tif")

    def checkBox_toggled(self):
        if(self.checkBox_buatModel.isChecked() == True):
            self.checkBox_prediksiBaru.setEnabled(False)

            self.textEdit_dataSample.setEnabled(True)
            self.pushButton_dataSample.setEnabled(True)
            self.textEdit_outputModel.setEnabled(True)
            self.textEdit_dataBaru.setEnabled(False)
            self.pushButton_dataBaru.setEnabled(False)
            self.textEdit_objekModel.setEnabled(False)
            self.pushButton_objekModel.setEnabled(False)
            self.textEdit_dataKlasifikasi.setEnabled(False)
        elif(self.checkBox_prediksiBaru.isChecked() == True):
            self.checkBox_buatModel.setEnabled(False)

            self.textEdit_dataSample.setEnabled(False)
            self.textEdit_outputModel.setEnabled(False)
            self.textEdit_dataBaru.setEnabled(True)
            self.pushButton_dataBaru.setEnabled(True)
            self.textEdit_objekModel.setEnabled(True)
            self.pushButton_objekModel.setEnabled(True)
            self.textEdit_dataKlasifikasi.setEnabled(True)
        else:
            self.checkBox_buatModel.setEnabled(True)
            self.checkBox_prediksiBaru.setEnabled(True)
            self.textEdit_dataSample.setEnabled(False)
            self.pushButton_dataSample.setEnabled(False)
            self.textEdit_outputModel.setEnabled(False)
            self.textEdit_dataBaru.setEnabled(False)
            self.pushButton_dataBaru.setEnabled(False)
            self.textEdit_objekModel.setEnabled(False)
            self.pushButton_objekModel.setEnabled(False)
            self.textEdit_dataKlasifikasi.setEnabled(False)


    def msgbtn(self):
        print "Button pressed is:"
        
    def showBox(self, text, info, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setInformativeText(info)
        msg.setWindowTitle(title)
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)

        retval = msg.exec_()
        print "value of pressed message box button:", retval


    def executeCode(self):
        msgRun = QMessageBox(self)

        msgRun.setAttribute(Qt.WA_DeleteOnClose)
        msgRun.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msgRun.setIcon(QMessageBox.Warning)
        msgRun.setBaseSize(QSize(1000, 500))

        msgRun.setText("Please wait, Its better to keep this dialog open")
        msgRun.setWindowTitle("Running")
        msgRun.setStandardButtons(QMessageBox.Ignore)
        msgRun.setWindowModality(Qt.NonModal);
        QCoreApplication.processEvents()
        msgRun.show()
        QCoreApplication.processEvents()

        if(self.checkBox_buatModel.isChecked() == True):

            print self.textEdit_dataSample.toPlainText()
            print self.textEdit_outputModel.toPlainText()

            modelFile = os.path.basename(self.textEdit_outputModel.toPlainText())
            akurasi = mm.makeModel(self.textEdit_dataSample.toPlainText(), self.textEdit_outputModel.toPlainText())
            print 'finished'
            msgRun.close()
            self.showBox("finished", "Kamu dapat memprediksi data baru dengan model yang telah disimpan", "Selesai...")
            self.label_akurasi.setText(modelFile+ '\n' +akurasi + ' %')
        else:
            print self.textEdit_dataBaru.toPlainText()
            print self.textEdit_objekModel.toPlainText()
            print self.textEdit_dataKlasifikasi.toPlainText()

            pc.predictClass(self.textEdit_dataBaru.toPlainText(), self.textEdit_objekModel.toPlainText(), self.textEdit_dataKlasifikasi.toPlainText())
            print 'finished'
            msgRun.close()
            self.showBox("finished", "Prediksi selesai, Kamu dapat menutup program ini sekarang", "Selesai...")

        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


