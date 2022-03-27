import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from main import post_tweet, getWeatherData
from pprint import pprint
from arduinocom import connectArd
import webbrowser
import serial
import threading
import time


class App(QtWidgets.QMainWindow):
    
    
    
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_post.clicked.connect(self.post)
        self.ui.btn_quickPost.clicked.connect(self.post)
        self.ui.btn_temp.clicked.connect(self.getTemp)
        self.ui.btn_connect_arduino.clicked.connect(self.startConnection)
        self.ui.btn_connect_arduino_2.clicked.connect(self.stopConnection)
        self.ui.btn_send.clicked.connect(self.sendLog)
        self.ui.btn_link_twitter.clicked.connect(self.goToLink)
        self.ui.btn_link_weather.clicked.connect(self.goToLink)
        self.ui.checkBox_manual.stateChanged.connect(self.activateText)
        
        
    def activateText(self):
        stat = self.sender().isChecked()
        if stat:
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.comboBox.setEnabled(False)
            self.ui.lineEdit_2.setText("")
        else:
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.comboBox.setEnabled(True)
            self.ui.lineEdit_2.setText("")
    
    def goToLink(self):
        button_name = self.sender().objectName()
        url_weather = "https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=36.8744&lon=30.6313&zoom=4"
        url_twitter  ="https://twitter.com/havni25"
        if button_name == "btn_link_twitter":
            webbrowser.open(url_twitter)
        elif button_name == "btn_link_weather":
            webbrowser.open(url_weather)
        
        
    def connectArduino(self):
        print("connect arduino")
        ser = serial.Serial()
        print("serial object created")
        ser.baudrate = 9600
        print("baudrate set")
        ser.port = 'COM7'
        print("port set")
        ser.open()
        print("serial port opened")
        while True:
            if ser.in_waiting:
                line = ser.readline()
                print(line.decode("utf-8").rsplit("\r\n")[0]) 
                tempVal = line.decode("utf-8").rsplit("\r\n")[0] 
                self.ui.lcd_ard.setProperty("value", tempVal)      

    def startConnection(self):
        t1.start()

    def stopConnection(self):
        pass       
    
    def sendLog(self):
        print("send log") 
        
    def getTemp(self):
        
        selected_city = self.ui.comboBox.currentText()
        
        if self.ui.lineEdit_2.isEnabled() and self.ui.lineEdit_2.text() != "":
            selected_city = self.ui.lineEdit_2.text()        
        
        print(selected_city)
        if selected_city != "" and selected_city is not None:
            try:
                jsonData = getWeatherData(selected_city)
                t = jsonData["main"]["temp"]
                self.ui.lcd_result.setProperty("value", t)
                self.ui.lineEdit_2.setText("")
                self.ui.lbl_selected_city.setText(selected_city)
            except Exception as e:
                print(e)
        
        
    def post(self):
        btn_name = self.sender().objectName()
        if btn_name == "btn_post":
            result = self.ui.txt_tweet.toPlainText()
            if result != "" and result is not None:
                try:
                    post_tweet(result)
                    self.ui.txt_tweet.setText("")
                    print("tweet posted!!")
                    QMessageBox.about(self, "Success!!", "Tweet posted!!")
                except Exception as e:
                    print(e)
                    QMessageBox.about(self, "Error!", "duplicate tweet!!!")
            else: 
                print("couldn't post tweet. Empty text.")
        elif btn_name == "btn_quickPost":
            city_name = self.ui.lbl_selected_city.text()
            temp = self.ui.lcd_result.value()
            if city_name != "" and city_name is not None :
                result = "Weather in " + city_name + " is " + str(temp) + " °C"
                try:
                    post_tweet(result)
                    print("tweet posted!!")
                    QMessageBox.about(self, "Success!!", "Tweet posted!!")
                except Exception as e:
                    print(e)
                    QMessageBox.about(self, "Error!", "duplicate tweet!!!")
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


t1 = threading.Thread(target=App.connectArduino, args=(App,))

app()    



