import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.setWindowTitle("AutoTwitter")
#         self.setGeometry(300,300,500,500)
#         self.setWindowIcon(QIcon("twitter.png"))
#         self.setToolTip("qwe")    
#         self.initUI()
        
#     def initUI(self):
#         self.label_name = QtWidgets.QLabel(self)
#         self.label_name.setText("name")

# def window():
#     app = QtWidgets.QApplication(sys.argv)
#     win = MyWindow()  
    
#     win.show()
#     sys.exit(app.exec_())
    
# window()

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())

app()    



