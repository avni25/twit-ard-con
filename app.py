import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from main import post_tweet, getWeatherData
from pprint import pprint


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_post.clicked.connect(self.post)
        self.ui.btn_temp.clicked.connect(self.getTemp)
        self.ui.btn_connect_arduino.clicked.connect(self.asd)
        self.ui.btn_send.clicked.connect(self.asd)
        
    def asd(self):
        print("show") 
        
    def getTemp(self):
        selected_city = self.ui.comboBox.currentText()
        print(selected_city)
        if selected_city != "" and selected_city is not None:
            try:
                jsonData = getWeatherData(selected_city)
                pprint(jsonData["main"]["temp"])
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



