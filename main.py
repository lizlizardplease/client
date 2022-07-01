from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from uimainw import Ui_MainWindow
from PyQt5.QtCore import QDataStream, QByteArray, QIODevice, qDebug
from searcher import Searcher
from changedata import DataChanger
import sys
import pickle
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtCore import pyqtSignal, QObject

testing_ghouls = ['マchen abuzerマ hate toxic', 'blood tears watch me die', '2-5 pos or feed immortal']


# потом удалю


class MainWindow(QMainWindow):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.chat_name = 'self chat'  # по дефолту изначально открыта переписка с собой
        self.socket = QTcpSocket(self)
        self.socket.connectToHost("127.0.0.1", 2323, QIODevice.OpenModeFlag.ReadWrite)
        self.data_ba = QByteArray()
        self.data_ba.clear()
        out = QDataStream(self.data_ba)
        out.setVersion(QDataStream.Qt_5_12)
        str = 'd' + name
        out.writeQString(str)
        self.socket.write(self.data_ba)
        self.chats = ['blood tears watch me die']  # сюда из бд все чаты, которые создал гуль
        self.inf = ['aaa', 'bbb', 1, 1, 1, 1] #сюда из бд приват дата
        self.ghouls = testing_ghouls #сюда пользователи из бд
        self.searcher = Searcher(self.ghouls)
        self.data_change = DataChanger(self.inf)
        self.setupUi(name)

    def setupUi(self, name):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myname = name
        self.filename = self.myname + '.pickle'
        self.listmodel = QStandardItemModel()
        self.ui.listView.setModel(self.listmodel)
        for i in self.chats:
            item = QStandardItem(i)
            self.listmodel.appendRow(item)
        if 1:  # тут типо проверка начата ли эта перепска, но запись об этом в бд, так что пока так
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        else:
            self.data = ['пока кать : мне на тебя покакать']
        self.messagemodel = QStandardItemModel()
        self.ui.listView_2.setModel(self.messagemodel)
        for i in self.data:
            item = QStandardItem(i)
            self.messagemodel.appendRow(item)
        self.ui.chat.clicked.connect(self.searchClicked)
        self.ui.data.clicked.connect(self.dataClicked)
        self.ui.send.clicked.connect(self.sendClicked)
        self.ui.listView.clicked.connect(self.picked)
        self.socket.readyRead.connect(self.getmessage)
        self.data_change.accepted.connect(self.update_data)
        self.searcher.accepted.connect(self.update_chats)
        # self.socket.disconnected.connect(self.socket.deleteLater())
        # че ему в этот deletelater передать, не поняла вообще

    def searchClicked(self):
        if(self.searcher.exec() == QDialog.Accepted):
            qDebug('fine')
            self.chats.append(self.searcher.chat_name)
            msg = 's' + self.myname + ',' + self.searcher.selected
            self.data_ba.clear()
            out = QDataStream(self.data_ba)
            out.setVersion(QDataStream.Qt_5_12)
            out.writeQString(msg)
            self.socket.write(self.data_ba)
            self.listmodel.appendRow(QStandardItem(self.searcher.chat_name))
            self.ui.listView.update()

    def update_data(self):
        if self.inf != self.data_change.my_inf:
            self.inf = self.data_change.my_inf
            msg = 'd' + self[0] + ',' + self[1] + ',' + self[2] + ',' + self[3] + ',' + self[4] + ',' + self[5]
            self.data_ba.clear()
            out = QDataStream(self.data_ba)
            out.setVersion(QDataStream.Qt_5_12)
            out.writeQString(msg)
            self.socket.write(self.data_ba)


    def dataClicked(self):
         self.data_change.exec()

    def sendClicked(self):
        if self.ui.textEdit.toPlainText() != '':
            msg = self.myname + ' : ' + self.ui.textEdit.toPlainText()
            self.data.append(msg)
            with open(self.filename, 'wb') as f:
                pickle.dump(self.data, f)
            self.ui.textEdit.clear()
            self.messagemodel.appendRow(QStandardItem(msg))
            self.ui.listView_2.update()
            f.close()
            msg = 'm' + msg
            data_ba = QByteArray()
            data_ba.clear()
            out = QDataStream(data_ba)
            out.setVersion(QDataStream.Qt_5_12)
            out.writeQString(msg)
            self.socket.write(data_ba)

    def getmessage(self):
        data = QDataStream(self.socket)
        data.setVersion(QDataStream.Qt_5_12)
        if data.status() == QDataStream.Ok:
            mssg = data.readQString()
            if mssg[0] == 'm':
                self.data.append(mssg)  # mssg - "mname : text"
                with open(self.filename, 'wb') as f:
                    pickle.dump(self.data, f)
                self.ui.textEdit.clear()
                self.messagemodel.appendRow(QStandardItem(mssg))
                self.ui.listView_2.update()
                f.close()
            if mssg[0] == 'd':  # mssg - "d, status, gay, cursed, gnf, abuzer"
                self.inf = mssg.split(",")
                self.inf[0] = self.myname
            if mssg[0] == 'c':
                self.chats == mssg.split(",")
                if len(self.chats) == 0:
                    self.chats.append(self.myname)
                else:
                    self.chats[0] == self.myname     #типо по дефолту есть чат с собой
            if mssg[0] == 'g':
                self.ghouls == mssg.split(',')
        # по-хорошему обработать ошибку иначе

    def picked(self, index):
        self.chat_name = self.listmodel.itemFromIndex(index).text()
        self.ui.label_2.setText(self.chat_name)
        self.filename = self.chat_name + '.pickle'
        if self.chat_name not in self.chats:
            self.chats.append(self.chat_name)
            f = open(self.filename, 'w')
            f.close()
            self.data = []
        else:
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        self.messagemodel = QStandardItemModel()
        self.ui.listView_2.setModel(self.messagemodel)
        for i in self.data:
            item = QStandardItem(i)
            self.messagemodel.appendRow(item)


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
        self.signin.clicked.connect(self.signinClicked)
        self.signup.clicked.connect(self.signupClicked)

    def signinClicked(self):
        lg = self.login.text()
        psw = self.password.text()
        # отправить их на сервер на проверку, с сигналом вход
        if 0:  # если сервер апрувнул
            self.cams = MainWindow('cursed')  # сюда передать lg
            self.cams.show()
            self.close()
        else:
            self.bad_news.setText("Error: wrong login or password")

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
        # отправить регистрацию на сервер
        self.cams = MainWindow('cursed')  # сюда передать lg
        self.cams.show()
        self.close()


if __name__ == "__main__":
    sys.stderr = open("stderr.txt", 'w')
    app = QApplication(sys.argv)
    win = Initialization()
    win.show()
    sys.exit(app.exec_())
    sys.stderr.close()