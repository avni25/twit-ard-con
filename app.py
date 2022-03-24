import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from main import post_tweet


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_post.clicked.connect(self.post)

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



