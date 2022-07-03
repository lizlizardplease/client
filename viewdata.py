from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from otherdata import Ui_Dialog
from PyQt5.QtCore import QDataStream, QByteArray


class OtherData(QDialog):
    def __init__(self, socket, ghoul, parent=None):
        super().__init__(parent)
        self.setupUi(socket, ghoul)

    def setupUi(self, socket, ghoul):
        super(OtherData, self).__init__()
        self.socket = socket
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        data_ba = QByteArray()
        data_ba.clear()
        out = QDataStream(data_ba)
        out.setVersion(QDataStream.Qt_5_12)
        str = 'a' + ghoul
        out.writeQString(str)
        self.ui.name.setText(ghoul)
        self.socket.write(data_ba)
        self.socket.readyRead.connect(self.getmessage)
        self.ui.pushButton.clicked.connect(self.ok)

    def ok(self):
        self.close()

    def getmessage(self):
        data = QDataStream(self.socket)
        data.setVersion(QDataStream.Qt_5_12)
        if data.status() == QDataStream.Ok:
            mssg = data.readQString()
            inf = mssg.split(',')
            self.ui.status.setText(inf[1])
            lbls = [self.ui.gay, self.ui.cursed, self.ui.gnf, self.ui.abuzer]
            for i in range(2, 6):
                if (inf[i]):
                    lbls[i - 2].setText("Yes")
                else:
                    lbls[i - 2].setText("No")
