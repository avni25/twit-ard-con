import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from main import TwitterAccount, getWeatherData
from pprint import pprint
from arduinocom import readPort
import webbrowser
import serial
import serial.tools.list_ports
import threading
import time
from datetime import datetime
from styles import *




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
        self.ui.btn_send.clicked.connect(self.addLog)
        self.ui.btn_link_twitter.clicked.connect(self.goToLink)
        self.ui.btn_link_weather.clicked.connect(self.goToLink)        
        self.ui.checkBox_manual.stateChanged.connect(self.activateText)
        self.ui.checkBox_isAuto.stateChanged.connect(self.setAutoSent)    
        self.ui.btn_tweetArduinoTemp.clicked.connect(self.setAutoSent)     
        self.t1 = threading.Thread(target=self.connectArduino)        
        self.t1_stop = False
        self.isAuto = False
        self.logText = ""
        ports = list(serial.tools.list_ports.comports())
        for p in ports:            
            print(p)
        
        
    def setAutoSent(self):
        self.isAuto = not self.isAuto
        print(self.isAuto)
            
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
            self.sendLog("Opened twitter")
        elif button_name == "btn_link_weather":
            webbrowser.open(url_weather)
            self.sendLog("Opened weather")
        
    
    def connectArduino(self):
        print("connect arduino")
        ser = serial.Serial()
        print("serial object created")
        ser.baudrate = 9600
        print("baudrate set")
        ser.port = self.ui.comboBox_port.currentText()
        print("port set")
        ser.open()
        print("serial port opened")          
        while True:
            if not self.t1_stop:                           
                if ser.in_waiting:
                    line = ser.readline()
                    # print(line.decode("utf-8").rsplit("\r\n")[0])
                    res = line.decode("utf-8").rsplit("\r\n")[0]
                    time.sleep(0.5)
                    print(res)
                    try:
                        self.printTemp(res)
                        
                    except Exception as e:
                        print(e)                    
                        pass
            
                    
    
    def printTemp(self, temp):
        self.ui.lcd_ard.setProperty("value", temp)                

    def startConnection(self):       
        
        self.sendLog("Arduino started")        
        try:
            self.t1.start()   
            self.ui.lbl_connecton_status.setStyleSheet("color: green")            
            self.ui.lbl_connecton_status.setText("connected")                     
        except Exception as e:
            print(e)
            pass

    def stopConnection(self):
        self.t1_stop = not self.t1_stop
        if self.t1_stop:
            self.ui.lbl_connecton_status.setStyleSheet("color: red")
            self.ui.lbl_connecton_status.setText("disconnected")
            self.sendLog("Arduino stopped")  
            self.ui.btn_connect_arduino_2.setText("resume")
            self.ui.btn_connect_arduino_2.setStyleSheet(style_btn_resume)
        else:
            self.ui.lbl_connecton_status.setStyleSheet("color: green")
            self.ui.lbl_connecton_status.setText("connected")
            self.sendLog("Arduino started")
            self.ui.btn_connect_arduino_2.setText("pause")
            self.ui.btn_connect_arduino_2.setStyleSheet(style_btn_pause)
    
    def sendLog(self, text):
        time = datetime.now()
        s = time.strftime("%d-%m-%Y %H:%M:%S")
        sb = self.logText
        self.logText = s+">>>"+text + "\n"+sb  
        self.ui.textedit_log.setPlainText(self.logText) 
     
    def addLog(self):
        
        try:
            s = self.ui.lineEdit_log.text();
            # ******************************
            #  komut kontrol
            # *************************
            self.sendLog(s)
            self.ui.lineEdit_log.setText("");
        except Exception as e:
            print(e)
            pass
        
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
                self.sendLog("Temperature query successful for "+selected_city+". result: "+str(t))
                self.ui.lineEdit_2.setText("")
                self.ui.lbl_selected_city.setText(selected_city)
            except Exception as e:
                print(e)
                self.sendLog("Error getting temperature. "+e)
        
        
    def post(self):
        btn_name = self.sender().objectName()
        account = TwitterAccount()
        if btn_name == "btn_post":
            result = self.ui.txt_tweet.toPlainText()
            if result != "" and result is not None:
                try:
                    # post_tweet(result)
                    account.post(result)
                    self.ui.txt_tweet.setText("")
                    print("tweet posted!!")
                    self.sendLog("Tweet posted: "+result)
                    QMessageBox.about(self, "Success!!", "Tweet posted!!")
                except Exception as e:
                    print(e)
                    QMessageBox.about(self, "Error!", "duplicate tweet!!!")
            else: 
                print("couldn't post tweet. Empty text.")
                self.sendLog("Error: attempted to post empty tweet")
        elif btn_name == "btn_quickPost":
            city_name = self.ui.lbl_selected_city.text()
            temp = self.ui.lcd_result.value()
            if city_name != "" and city_name is not None :
                result = "Weather in " + city_name + " is " + str(temp) + " °C"
                try:
                    account.post(result)
                    print("tweet posted!!")
                    self.sendLog("Quick Tweet posted: "+result)
                    QMessageBox.about(self, "Success!!", "Tweet posted!!")
                except Exception as e:
                    print(e)
                    self.sendLog("Error: attempted to post duplicate tweet")
                    QMessageBox.about(self, "Error!", "duplicate tweet!!!")
        elif btn_name == "lbl_autoTweet":
            print("auto tweet")
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())


 
# t1 = threading.Thread(target=App.connectArduino, args=(App,))


app()    



