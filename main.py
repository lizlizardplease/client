from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mymain import Ui_MainWindow
from searcher import Searcher
from changedata import DataChanger
from comunicator import Comunicator
import sys
import pickle
from init import Initialization


testing_ghouls = ['マchen abuzerマ hate toxic', 'blood tears watch me die', '2-5 pos or feed immortal']
# потом удалю


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.chat_name = 'self chat'  # по дефолту изначально открыта переписка с собой
        self.to_artem = Comunicator()
        self.initer = Initialization()
        self.initer.enter.connect(self.enters)
        self.to_artem.client_comes.connect(self.comes)
        self.to_artem.message_received.connect(self.getmessage)
        if self.initer.exec_() == QDialog.Accepted:
            self.environment()


    def setupUi(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagemodel = QStandardItemModel()
        self.listmodel = QStandardItemModel()
        self.ui.listView.setModel(self.listmodel)
        self.ui.chat.clicked.connect(self.searchClicked)
        self.ui.data.clicked.connect(self.dataClicked)
        self.ui.send.clicked.connect(self.sendClicked)
        self.ui.listView.clicked.connect(self.picked)
        # self.socket.disconnected.connect(self.socket.deleteLater())
        # че ему';
        # в этот deletelater передать, не поняла вообще

    def environment(self):
        self.inf = ['aaa', 'bbb', 1, 1, 1, 1]  # сюда из бд приват дата
        self.ghouls = testing_ghouls  # сюда пользователи из бд
        str = 'g' + self.myname
        self.not_my = 0
        self.chats = []
        self.to_artem.ask(str)
        self.messgs = {}
        self.filename = self.myname + '.pickle'
        if (1):
            f = open(self.filename, 'w')
            f.close()
            self.messgs[self.chat_name] = []
        else:
            with open(self.filename, 'rb') as f:
                self.messgs = pickle.load(f)
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



    def friending(self, ghoul):
        q = 'a' + ghoul
        print(q)
        self.not_my = 1
        self.to_artem.ask(q)

    def searchClicked(self):
        if self.searcher.exec_() == QDialog.Accepted:
            self.messgs[self.searcher.chat_name] = []
            msg = 's' + self.searcher.chat_name + ':' + self.myname + ',' + self.searcher.selected
            self.to_artem.ask(msg)
            self.listmodel.appendRow(QStandardItem(self.searcher.chat_name))
            self.ui.listView.update()

    def dataClicked(self):
        if self.data_change.exec_() == QDialog.Accepted:
            self.inf = self.data_change.my_inf
            msg = 'd' + self.inf[0] + ',' + self.inf[1] + ',' + str(self.inf[2]) + ',' + str(self.inf[3]) + ',' + str(self.inf[4]) + ',' + str(self.inf[5])
            self.to_artem.ask(msg)


    def enters(self, strr):
        print(strr)
        self.to_artem.ask(strr)

    def comes(self, realy):
        if realy % 10 != 0:
            self.myname = self.initer.login.text()
            self.initer.accept()
        else:
            if realy == 11:
                self.initer.bad_news.setText("Error: wrong login or password")
            else:
                self.initer.bad_news.setText("Login is already used. Try another one.")

    def sendClicked(self):
        if self.ui.textEdit.toPlainText() != '':
            msg = self.myname + ' : ' + self.ui.textEdit.toPlainText()
            self.messgs[self.chat_name].append(msg)
            self.messagemodel.appendRow(QStandardItem(msg))
            self.ui.listView_2.update()
            self.to_artem.send_message(self.chat_name, self.myname, self.ui.textEdit.toPlainText()) #можно проще
            self.ui.textEdit.clear()


    def getmessage(self, mssg):
        print(mssg)
        if mssg[0] == 'm':
            mssgl = mssg.split(',')
            self.messgs[mssgl[0][1:]].append(mssgl[1])
            self.ui.textEdit.clear()
            self.messagemodel.appendRow(QStandardItem(mssg))
            self.ui.listView_2.update()
        if mssg[0] == 'd':
            print(mssg)
            if self.not_my:
                self.searcher.go_data(mssg)
                self.not_my = 0
            else:
                self.inf = mssg.split(",")
                self.inf[0] = self.myname
        if mssg[0] == 'v':
            self.chats.append(mssg[1:])
        if mssg[0] == 'c':
            for i in mssg.split(","):
                self.chats.append(i)
                self.listmodel.appendRow(QStandardItem(i))
            if len(self.chats) == 0:
               self.chats.append(self.myname)
        if mssg[0] == '~':
            z = mssg[2:].split('@')
            for i in z[1].split(","):
                self.chats.append(i)
                self.listmodel.appendRow(QStandardItem(i))
            if len(self.chats) == 0:
               self.chats.append(self.myname)
            tmp = z[0].split(',')
            self.ghouls = tmp[7:]
            self.inf = tmp[:6]
            print(self.ghouls)
            print(self.inf)
            self.searcher = Searcher(self.ghouls)
            print('zxc')
            self.inf[0] = self.myname
            print('zxc')
            self.data_change = DataChanger(self.inf)
            print('zxc')
            print('zxc')
            self.searcher.is_friend.connect(self.friending)
            print('zxc')

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





if __name__ == "__main__":
    sys.stderr = open("stderr.txt", 'w')
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
