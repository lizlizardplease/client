from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from otherdata import Ui_Dialog
from PyQt5 import QtCore


class OtherData(QDialog):
    def __init__(self, mssg, parent=None):
        super().__init__(parent)
        self.setupUi(mssg)

    def setupUi(self, mssg):
        super(OtherData, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        inf = mssg.split(',')
        self.ui.status.setText(inf[1])
        lbls = [self.ui.gay, self.ui.cursed, self.ui.gnf, self.ui.abuzer]
        for i in range(2, 6):
            if (inf[i]):
                lbls[i - 2].setText("Yes")
            else:
                lbls[i - 2].setText("No")
        self.ui.name.setText(inf[0])
        self.ui.pushButton.clicked.connect(self.ok)

    def ok(self):
        self.close()
