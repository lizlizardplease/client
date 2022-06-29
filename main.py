from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from uimainw import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from searcher import Searcher
from changedata import DataChanger
from tablemodel import TableModel
import csv
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chats = []
        self.chat_name = 'self chat'
        self.setupUi()


    def setupUi(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myname = 'cursed'
        self.filename = self.myname + '.csv'
        f = open(self.filename, 'w')
        f.close()
        self.data = []
        with open(self.filename) as data_file:
            for line in data_file:
                self.data.append(line.strip().split(';'))
        self.ui.chat.clicked.connect(self.searchClicked)
        self.ui.data.clicked.connect(self.dataClicked)
        self.ui.send.clicked.connect(self.sendClicked)
        #self.ui.listWidget.itemClicked(self.choosen)
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)


    def searchClicked(self):
        self.cams = Searcher()
        self.cams.show()

    def dataClicked(self):
        self.cams = DataChanger()
        self.cams.show()

    def sendClicked(self):
        if self.chat_name not in self.chats:
            self.chats.append(self.chat_name)
            self.filename = self.chat_name + '.csv'
        if self.ui.textEdit.toPlainText() != '':
            with open(self.filename, "a", newline="") as file:
                mssg = [self.myname, self.ui.textEdit.toPlainText()]
                writer = csv.writer(file)
                writer.writerow(mssg)
            # self.model.insertRow(self, self.model.rowCount())
            self.ui.textEdit.clear()

    #def choosen(self, item):
    #    self.ui.label_2.setText(item.text())
     #   if self.chat_name not in self.chats:
     #       self.chats.append(self.chat_name)
      #      self.filename = self.chat_name + '.csv'


class Initialization(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Welcome")
        self.move(300, 300)
        self.resize(800, 600)
        with open("init.qss", "r") as file:
            style = file.read()
        self.setStyleSheet(style)
        self.lbl = QLabel('welcome to hopeless "i tired of this place" zxc god chat ', self)
        self.lbl.setObjectName("heading")
        self.lbl.move(30, 30)
        self.lbl1 = QLabel(self)
        self.pix = QPixmap("resources\zxc1.jpg")
        self.lbl1.setPixmap(self.pix)
        self.lbl1.move(80, 80)
        self.lbl1.setFixedWidth(680)
        self.lbl1.setFixedHeight(350)
        self.lbl2 = QLabel('要login要彡彡彡', self)
        self.lbl2.move(30, 450)
        self.lbl3 = QLabel('鎰鎰password', self)
        self.lbl3.move(30, 490)
        self.signin = QPushButton('sign in', self)
        self.signup = QPushButton('sign up', self)
        self.signup.setObjectName("signup")
        self.signin.move(70, 530)
        self.signup.move(470, 530)
        self.signin.setObjectName("signin")
        self.login = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.move(200, 490)
        self.login.move(200, 450)
        self.password.setEchoMode(QLineEdit.Password)
        self.signin.clicked.connect(self.signinClicked)

    def signinClicked(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Initialization()
    win.show()
    sys.exit(app.exec_())
