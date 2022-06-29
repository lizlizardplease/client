from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from uiprivatedata import Ui_Dialog
from PyQt5.QtCore import pyqtSignal, QObject


class DataChanger(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.changing = 0

    def setupUi(self):
        super(DataChanger, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.away.clicked.connect(self.exitClicked)
        self.ui.change.clicked.connect(self.changeClicked)

    def changeClicked(self):
        if self.changing == 1:
            self.ui.change.setText("Change private data")
        else:
            self.ui.change.setText("Done")
        self.ui.login.setReadOnly(self.changing)
        self.ui.status.setReadOnly(self.changing)
        self.changing += 1
        self.changing %= 2

    def exitClicked(self):
        self.close()