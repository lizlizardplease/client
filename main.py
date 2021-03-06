from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from uimainw import Ui_MainWindow
from PyQt5.QtCore import QDataStream, QByteArray, QIODevice
from searcher import Searcher
from changedata import DataChanger
import sys
import pickle
from PyQt5.QtNetwork import QTcpSocket


testing_ghouls = ['マchen abuzerマ hate toxic', 'blood tears watch me die', '2-5 pos or feed immortal']


# потом удалю


class MainWindow(QMainWindow):
    def __init__(self, name, socket, parent=None):
        super().__init__(parent)
        self.chat_name = 'self chat'  # по дефолту изначально открыта переписка с собой
        self.socket = socket
        self.myname = name[1:]
        str = 'a' + self.myname
        self.socket.write(str.encode('utf-8'))
        self.messgs = {}
        self.inf = ['aaa', 'bbb', 1, 1, 1, 1]  # сюда из бд приват дата
        str = 'g'
        self.socket.write(str.encode('utf-8'))
        self.ghouls = testing_ghouls  # сюда пользователи из бд
        self.searcher = Searcher(self.ghouls, socket)
        self.data_change = DataChanger(self.inf)
        self.setupUi(name, socket)


    def setupUi(self, name, socket):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagemodel = QStandardItemModel()
        self.listmodel = QStandardItemModel()
        self.filename = self.myname + '.pickle'
        if (1):
            f = open(self.filename, 'w')
            f.close()
            self.messgs[self.chat_name] = []
        else:
            with open(self.filename, 'rb') as f:
                self.messgs = pickle.load(f)
        self.ui.listView.setModel(self.listmodel)
        for i in self.messgs.keys():
            item = QStandardItem(i)
            self.listmodel.appendRow(item)
        if self.chat_name in self.messgs.keys():
            pass
        else:
            self.messgs[self.chat_name] = []

        self.ui.listView_2.setModel(self.messagemodel)
        for i in self.messgs[self.chat_name]:
            item = QStandardItem(i)
            self.messagemodel.appendRow(item)
        self.ui.chat.clicked.connect(self.searchClicked)
        self.ui.data.clicked.connect(self.dataClicked)
        self.ui.send.clicked.connect(self.sendClicked)
        self.ui.listView.clicked.connect(self.picked)
        self.socket.readyRead.connect(self.getmessage)
        # self.socket.disconnected.connect(self.socket.deleteLater())
        # че ему в этот deletelater передать, не поняла вообще

    def searchClicked(self):
        if self.searcher.exec_() == QDialog.Accepted:
            self.messgs[self.searcher.chat_name] = []
            msg = 's' + self.searcher.chat_name + ':' + self.myname + ',' + self.searcher.selected
            self.socket.write(msg.encode('utf-8'))
            self.listmodel.appendRow(QStandardItem(self.searcher.chat_name))
            self.ui.listView.update()

    def dataClicked(self):
        if self.data_change.exec_() == QDialog.Accepted:
            self.inf = self.data_change.my_inf
            msg = 'd' + self.inf[0] + ',' + self.inf[1] + ',' + str(self.inf[2]) + ',' + str(self.inf[3]) + ',' + str(self.inf[4]) + ',' + str(self.inf[5])
            self.socket.write(msg.encode('utf-8'))

    def sendClicked(self):
        if self.ui.textEdit.toPlainText() != '':
            msg = self.myname + ' : ' + self.ui.textEdit.toPlainText()
            self.messgs[self.chat_name].append(msg)
            self.ui.textEdit.clear()
            self.messagemodel.appendRow(QStandardItem(msg))
            self.ui.listView_2.update()
            msg = 'm' + self.chat_name + ','+ msg
            self.socket.write(msg.encode('utf-8'))

    def getmessage(self):
        mssg = self.socket.read(1024).decode('utf-8')
        if mssg[0] == 'm':
            mssgl = mssg.split(',')
            self.messgs[mssgl[0][1:]].append(mssgl[1])
            self.ui.textEdit.clear()
            self.messagemodel.appendRow(QStandardItem(mssg))
            self.ui.listView_2.update()
        if mssg[0] == 'd':  # mssg - "d, status, gay, cursed, gnf, abuzer"
            self.inf = mssg.split(",")
            self.inf[0] = self.myname
            for i in self.inf[2:]:
                i = bool(i)
        if mssg[0] == 'c':
            for i in mssg.split(","):
                if len(self.chats) == 0:
                    self.chats.append(self.myname)
                else:
                    self.chats[0] == self.myname  # типо по дефолту есть чат с собой
        if mssg[0] == 'g':
            self.ghouls = mssg.split(',')
        # по-хорошему обработать ошибку иначе

    def picked(self, index):
        self.chat_name = self.listmodel.itemFromIndex(index).text()
        self.ui.label_2.setText(self.chat_name)
        if self.chat_name not in self.messgs.keys():
            self.messgs[self.chat_name] = []
        self.messagemodel = QStandardItemModel()
        self.ui.listView_2.setModel(self.messagemodel)
        for i in self.messgs[self.chat_name]:
            item = QStandardItem(i)
            self.messagemodel.appendRow(item)

    def closeEvent(self, event):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.messgs, f)
        self.socket.disconnectFromHost()



class Initialization(QDialog):
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
        self.socket = QTcpSocket(self)
        self.socket.connectToHost("localhost", 5431, QIODevice.OpenModeFlag.ReadWrite)
        self.data_ba = QByteArray()
        self.data_ba.clear()
        self.signin.clicked.connect(self.signinClicked)
        self.signup.clicked.connect(self.signupClicked)
        self.socket.readyRead.connect(self.signingin)

    def signingin(self):
        lg = 'e' + self.login.text()
        mssg = self.socket.read(1024).decode('utf-8')
        if mssg[1:] == 'accepted':  # если сервер апрувнул
            self.cams = MainWindow(lg, self.socket)
            self.cams.show()
            self.close()
        else:
            if mssg[0] == 'e':
                self.bad_news.setText("Error: wrong login or password")
            else:
                self.bad_news.setText("Login is already used. Try another one.")

    def signinClicked(self):
        lg = self.login.text()
        psw = self.password.text()
        str = 'e' + lg + ',' + psw
        self.socket.write(str.encode('utf-8'))
        self.bad_news.setText("Checking information......")

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
        lg = 'r' + self.login.text()
        psw = self.password.text()
        str = lg + ',' + psw
        self.socket.write(str.encode('utf-8'))
        self.cams = MainWindow(lg, self.socket)
        self.cams.show()
        self.close()


if __name__ == "__main__":
    sys.stderr = open("stderr.txt", 'w')
    app = QApplication(sys.argv)
    win = Initialization()
    win.show()
    sys.exit(app.exec_())

