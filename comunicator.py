from PyQt5.QtNetwork import QTcpSocket
from PyQt5 import QtCore



class Comunicator(QtCore.QObject):
    message_received = QtCore.pyqtSignal(str)
    user_connected = QtCore.pyqtSignal()
    client_comes = QtCore.pyqtSignal(int)

    def __init__(self, socket: QTcpSocket = None):
        """
        Initializes the extended TCP socket. Either wraps around an existing socket or creates its own and resets
        the number of bytes written.

        :param socket: An already existing socket or None if none is given.
        """
        super().__init__()

        # new QTcpSocket() if none is given
        if socket is not None:
            self.socket = socket
        else:
            self.socket = QTcpSocket()

        self.socket.connectToHost('172.20.10.7', 5431, QtCore.QIODevice.OpenModeFlag.ReadWrite)
        self.socket.readyRead.connect(self.handle_message)


    def handle_message(self):
        mssg = self.socket.read(1024).decode('utf-8')
        #mssg = 'eaccepted' #пока не соединяемся
        if mssg == '':
            return
        if mssg[0] == 'e':
            if mssg[1:] == 'accepted':  # если сервер апрувнул
                self.client_comes.emit(11)
            else:
                self.client_comes.emit(10)
        if mssg[0] == 'r':
            if mssg[1:] == 'accepted':
                self.client_comes.emit(21)
            else:
                self.client_comes.emit(20)
        else:
            self.message_received.emit(mssg)
        # по-хорошему обработать ошибку иначе

    def send_message(self, chat_name, name, data):
        if data != '':
            msg = 'm' + chat_name + ',' + name + ' : ' + data
            self.socket.write(msg.encode('utf-8'))


    def ask(self, question):
        self.socket.write(question.encode('utf-8'))
        print(question)

