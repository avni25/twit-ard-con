import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("AutoTwitter")
    win.setGeometry(300,300,500,500)
    win.setWindowIcon(QIcon("twitter.png"))
    
    win.show()
    sys.exit(app.exec_())
    
window()




