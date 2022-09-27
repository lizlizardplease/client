from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class Initialization(QDialog):
    enter = QtCore.pyqtSignal(str)
    leave = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Welcome")
        self.move(300, 0)
        self.resize(800, 620)
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
        self.bad_news = QLabel('', self)
        self.bad_news.setObjectName('error')
        self.bad_news.move(70, 580)
        self.bad_news.setFixedWidth(700)
        self.signin.clicked.connect(self.signinClicked)
        self.signup.clicked.connect(self.signupClicked)

    def signinClicked(self):
        strr = 'e' + self.login.text() + ',' + self.password.text()
        #strr = 'eaccepted'
        self.bad_news.setText("Checking information......")
        self.enter.emit(strr)

    def signupClicked(self):
        lg = self.login.text()
        psw = self.password.text()
        if len(lg) > 20:
            self.bad_news.setText("Login is too long!")
            return
        if len(psw) > 20:
            self.bad_news.setText("Password is too long!")
            return
        if len(lg) == 0:
            self.bad_news.setText("Login mustn't be empty!")
            return
        if len(psw) == 0:
            self.bad_news.setText("Password mustn't be empty!")
            return
        if not (lg.isalnum() and psw.isalnum()):
            self.bad_news.setText("Password and login must contain only latin letters and numbers!")
            return
        strr = 'r' + self.login.text() + ',' + self.password.text()
        self.enter.emit(strr)

