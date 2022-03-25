import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from main import post_tweet, getWeatherData
from pprint import pprint
import webbrowser

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_post.clicked.connect(self.post)
        self.ui.btn_quickPost.clicked.connect(self.post)
        self.ui.btn_temp.clicked.connect(self.getTemp)
        self.ui.btn_connect_arduino.clicked.connect(self.connectArduino)
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
        result = self.ui.txt_tweet.toPlainText()
        if result != "" and result is not None:
            post_tweet(result)
            self.ui.txt_tweet.setText("")
            print("tweet posted!!")
            QMessageBox.about(self, "Success!!", "Tweet posted!!")
        else: 
            print("couldn't post tweet. Empty text.")
        
    
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


app()    



