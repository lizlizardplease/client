from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mydesign import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QObject
import sysgit


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.change.clicked.connect(self.btnClicked)
        self.changing = 0

    def btnClicked(self):
        if (self.changing == 1):
            self.ui.change.setText("Change private data")
        else:
            self.ui.change.setText("Done")
        self.ui.login.setReadOnly(self.changing)
        self.ui.status.setReadOnly(self.changing)
        self.changing += 1
        self.changing %= 2

class Searcher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())