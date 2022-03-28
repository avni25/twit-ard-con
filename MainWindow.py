# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_twitter = QtWidgets.QGroupBox(self.centralwidget)
        self.group_twitter.setGeometry(QtCore.QRect(380, 300, 261, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.group_twitter.setFont(font)
        self.group_twitter.setStyleSheet("\n"
"color: rgb(28, 149, 255);")
        self.group_twitter.setObjectName("group_twitter")
        self.btn_post = QtWidgets.QPushButton(self.group_twitter)
        self.btn_post.setGeometry(QtCore.QRect(160, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_post.setFont(font)
        self.btn_post.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_post.setMouseTracking(False)
        self.btn_post.setToolTip("")
        self.btn_post.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(23, 96, 186);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    cursor: pointer;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: rgb(34, 178, 255);\n"
"    cursor: pointer;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("tw3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_post.setIcon(icon)
        self.btn_post.setObjectName("btn_post")
        self.label = QtWidgets.QLabel(self.group_twitter)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_tweet = QtWidgets.QTextEdit(self.group_twitter)
        self.txt_tweet.setGeometry(QtCore.QRect(10, 60, 241, 81))
        self.txt_tweet.setObjectName("txt_tweet")
        self.btn_link_twitter = QtWidgets.QPushButton(self.group_twitter)
        self.btn_link_twitter.setGeometry(QtCore.QRect(10, 200, 161, 23))
        self.btn_link_twitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_twitter.setStyleSheet("color: blue;")
        self.btn_link_twitter.setFlat(True)
        self.btn_link_twitter.setObjectName("btn_link_twitter")
        self.group_weatherapi = QtWidgets.QGroupBox(self.centralwidget)
        self.group_weatherapi.setGeometry(QtCore.QRect(380, 20, 261, 261))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.group_weatherapi.setFont(font)
        self.group_weatherapi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.group_weatherapi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.group_weatherapi.setStyleSheet("color: rgb(255, 68, 35);")
        self.group_weatherapi.setObjectName("group_weatherapi")
        self.lcd_result = QtWidgets.QLCDNumber(self.group_weatherapi)
        self.lcd_result.setGeometry(QtCore.QRect(10, 100, 181, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcd_result.setFont(font)
        self.lcd_result.setStyleSheet("color:red;")
        self.lcd_result.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_result.setLineWidth(2)
        self.lcd_result.setMidLineWidth(0)
        self.lcd_result.setSmallDecimalPoint(False)
        self.lcd_result.setDigitCount(7)
        self.lcd_result.setProperty("value", 0.0)
        self.lcd_result.setObjectName("lcd_result")
        self.comboBox = QtWidgets.QComboBox(self.group_weatherapi)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon.fromTheme("dark")
        self.comboBox.addItem(icon, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.group_weatherapi)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_temp = QtWidgets.QPushButton(self.group_weatherapi)
        self.btn_temp.setGeometry(QtCore.QRect(10, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_temp.setFont(font)
        self.btn_temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_temp.setStyleSheet("QPushButton{\n"
"    background-color: rgb(184, 61, 0);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    cursor: pointer;\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: rgb(255, 114, 44);\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"")
        self.btn_temp.setShortcut("")
        self.btn_temp.setCheckable(False)
        self.btn_temp.setChecked(False)
        self.btn_temp.setAutoDefault(False)
        self.btn_temp.setDefault(False)
        self.btn_temp.setFlat(False)
        self.btn_temp.setObjectName("btn_temp")
        self.checkBox_manual = QtWidgets.QCheckBox(self.group_weatherapi)
        self.checkBox_manual.setGeometry(QtCore.QRect(130, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_manual.setFont(font)
        self.checkBox_manual.setObjectName("checkBox_manual")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.group_weatherapi)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.group_weatherapi)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: red;")
        self.label_2.setObjectName("label_2")
        self.btn_link_weather = QtWidgets.QPushButton(self.group_weatherapi)
        self.btn_link_weather.setGeometry(QtCore.QRect(0, 230, 211, 23))
        self.btn_link_weather.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_weather.setStyleSheet("color: blue;")
        self.btn_link_weather.setDefault(False)
        self.btn_link_weather.setFlat(True)
        self.btn_link_weather.setObjectName("btn_link_weather")
        self.lbl_selected_city = QtWidgets.QLabel(self.group_weatherapi)
        self.lbl_selected_city.setGeometry(QtCore.QRect(10, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_selected_city.setFont(font)
        self.lbl_selected_city.setStyleSheet("color: red;")
        self.lbl_selected_city.setText("")
        self.lbl_selected_city.setObjectName("lbl_selected_city")
        self.btn_quickPost = QtWidgets.QPushButton(self.group_weatherapi)
        self.btn_quickPost.setEnabled(True)
        self.btn_quickPost.setGeometry(QtCore.QRect(140, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_quickPost.setFont(font)
        self.btn_quickPost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_quickPost.setMouseTracking(False)
        self.btn_quickPost.setToolTip("")
        self.btn_quickPost.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(23, 96, 186);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    cursor: pointer;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: rgb(34, 178, 255);\n"
"    cursor: pointer;\n"
"}\n"
"")
        self.btn_quickPost.setObjectName("btn_quickPost")
        self.group_arduino = QtWidgets.QGroupBox(self.centralwidget)
        self.group_arduino.setGeometry(QtCore.QRect(10, 30, 361, 501))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_arduino.setFont(font)
        self.group_arduino.setStyleSheet("")
        self.group_arduino.setObjectName("group_arduino")
        self.btn_connect_arduino = QtWidgets.QPushButton(self.group_arduino)
        self.btn_connect_arduino.setGeometry(QtCore.QRect(10, 30, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_connect_arduino.setFont(font)
        self.btn_connect_arduino.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_connect_arduino.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(23, 96, 186);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    cursor: pointer;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: rgb(34, 178, 255);\n"
"    cursor: pointer;\n"
"}")
        self.btn_connect_arduino.setObjectName("btn_connect_arduino")
        self.textedit_log = QtWidgets.QPlainTextEdit(self.group_arduino)
        self.textedit_log.setEnabled(True)
        self.textedit_log.setGeometry(QtCore.QRect(0, 190, 351, 271))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textedit_log.setFont(font)
        self.textedit_log.setStyleSheet("color: green;\n"
"background-color: black;")
        self.textedit_log.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textedit_log.setReadOnly(True)
        self.textedit_log.setCenterOnScroll(False)
        self.textedit_log.setObjectName("textedit_log")
        self.lineEdit_log = QtWidgets.QLineEdit(self.group_arduino)
        self.lineEdit_log.setGeometry(QtCore.QRect(0, 460, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_log.setFont(font)
        self.lineEdit_log.setStyleSheet("color: green;\n"
"background-color: black;")
        self.lineEdit_log.setObjectName("lineEdit_log")
        self.lbl_connecton_status = QtWidgets.QLabel(self.group_arduino)
        self.lbl_connecton_status.setEnabled(False)
        self.lbl_connecton_status.setGeometry(QtCore.QRect(220, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_connecton_status.setFont(font)
        self.lbl_connecton_status.setStyleSheet("color:green")
        self.lbl_connecton_status.setObjectName("lbl_connecton_status")
        self.label_4 = QtWidgets.QLabel(self.group_arduino)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_send = QtWidgets.QPushButton(self.group_arduino)
        self.btn_send.setGeometry(QtCore.QRect(290, 460, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_send.setFont(font)
        self.btn_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_send.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(23, 96, 186);\n"
"    color: white;    \n"
"    cursor: pointer;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: rgb(34, 178, 255);\n"
"    cursor: pointer;\n"
"}")
        self.btn_send.setObjectName("btn_send")
        self.lcd_ard = QtWidgets.QLCDNumber(self.group_arduino)
        self.lcd_ard.setGeometry(QtCore.QRect(220, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lcd_ard.setFont(font)
        self.lcd_ard.setDigitCount(6)
        self.lcd_ard.setObjectName("lcd_ard")
        self.btn_connect_arduino_2 = QtWidgets.QPushButton(self.group_arduino)
        self.btn_connect_arduino_2.setGeometry(QtCore.QRect(10, 80, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_connect_arduino_2.setFont(font)
        self.btn_connect_arduino_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_connect_arduino_2.setStyleSheet("QPushButton{    \n"
"    background-color: red;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    cursor: pointer;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{   \n"
"    background-color: gray;\n"
"    cursor: pointer;\n"
"}")
        self.btn_connect_arduino_2.setObjectName("btn_connect_arduino_2")
        self.lbl_autoTweet = QtWidgets.QLabel(self.group_arduino)
        self.lbl_autoTweet.setGeometry(QtCore.QRect(330, 100, 21, 21))
        self.lbl_autoTweet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_autoTweet.setText("")
        self.lbl_autoTweet.setPixmap(QtGui.QPixmap("tw3.ico"))
        self.lbl_autoTweet.setScaledContents(True)
        self.lbl_autoTweet.setObjectName("lbl_autoTweet")
        self.checkBox_isAuto = QtWidgets.QCheckBox(self.group_arduino)
        self.checkBox_isAuto.setGeometry(QtCore.QRect(210, 100, 111, 21))
        self.checkBox_isAuto.setObjectName("checkBox_isAuto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_twitter.setTitle(_translate("MainWindow", "Twitter"))
        self.btn_post.setText(_translate("MainWindow", "Post"))
        self.label.setText(_translate("MainWindow", "Tweet Content"))
        self.txt_tweet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_link_twitter.setText(_translate("MainWindow", "go to twitter account web page"))
        self.group_weatherapi.setTitle(_translate("MainWindow", "WeatherAPI"))
        self.comboBox.setItemText(0, _translate("MainWindow", "istanbul"))
        self.comboBox.setItemText(1, _translate("MainWindow", "antalya"))
        self.comboBox.setItemText(2, _translate("MainWindow", "berlin"))
        self.comboBox.setItemText(3, _translate("MainWindow", "london"))
        self.comboBox.setItemText(4, _translate("MainWindow", "moscow"))
        self.comboBox.setItemText(5, _translate("MainWindow", "paris"))
        self.comboBox.setItemText(6, _translate("MainWindow", "sydney"))
        self.comboBox.setItemText(7, _translate("MainWindow", "cape town"))
        self.comboBox.setItemText(8, _translate("MainWindow", "madrid"))
        self.comboBox.setItemText(9, _translate("MainWindow", "prague"))
        self.label_3.setText(_translate("MainWindow", "City name"))
        self.btn_temp.setText(_translate("MainWindow", "Get Temp"))
        self.checkBox_manual.setText(_translate("MainWindow", "type manual"))
        self.label_2.setText(_translate("MainWindow", "°C"))
        self.btn_link_weather.setText(_translate("MainWindow", "for more cities visit openweatehrmap.org"))
        self.btn_quickPost.setText(_translate("MainWindow", "Quick Post"))
        self.group_arduino.setTitle(_translate("MainWindow", "Arduino"))
        self.btn_connect_arduino.setText(_translate("MainWindow", "Connect"))
        self.textedit_log.setPlainText(_translate("MainWindow", "Logger:"))
        self.lbl_connecton_status.setText(_translate("MainWindow", "qwe"))
        self.label_4.setText(_translate("MainWindow", "Log"))
        self.btn_send.setText(_translate("MainWindow", "Send"))
        self.btn_connect_arduino_2.setText(_translate("MainWindow", "Stop"))
        self.lbl_autoTweet.setToolTip(_translate("MainWindow", "post arduino temperature to Twitter"))
        self.checkBox_isAuto.setText(_translate("MainWindow", "auto tweet"))
