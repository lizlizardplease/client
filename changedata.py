from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from uiprivatedata import Ui_Dialog
from PyQt5.QtCore import pyqtSignal, QObject


class DataChanger(QDialog):
    data_changed = pyqtSignal(str)
    def __init__(self, inf, parent=None):
        super().__init__(parent)
        self.setupUi(inf)
        self.changing = 0
        self.my_inf = inf
        self.changed = 0

    def setupUi(self, inf):
        super(DataChanger, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login.setText(inf[0])
        self.ui.status.setText(inf[1])
        self.ui.gay.setChecked(bool(inf[2]))
        print(bool(inf[4]))
        self.ui.cursed.setChecked(bool(inf[3]))
        self.ui.gnf.setChecked(bool(inf[4]))
        self.ui.abuzer.setChecked(bool(inf[5]))
        self.ui.login.setReadOnly(1)
        self.ui.status.setReadOnly(1)
        self.ui.gay.blockSignals(True)
        self.ui.gnf.blockSignals(1)
        self.ui.abuzer.blockSignals(1)
        self.ui.cursed.blockSignals(1)
        self.ui.away.clicked.connect(self.exitClicked)
        self.ui.change.clicked.connect(self.changeClicked)

    def changeClicked(self):
        if self.changing == 1:
            self.my_inf[0] = self.ui.login.text()
            self.ui.login.setReadOnly(1)
            self.my_inf[1] = self.ui.status.toPlainText()
            self.my_inf[2] = str(self.ui.gay.isChecked())
            self.my_inf[3] = str(self.ui.cursed.isChecked())
            self.my_inf[4] = str(self.ui.gnf.isChecked())
            self.my_inf[5] = str(self.ui.abuzer.isChecked())
            m = 'd' +','.join(self.my_inf)
            self.data_changed.emit(m)
            print('zxczxc')
            self.ui.change.setText("Change private data")
            self.changed = 1
        else:
            self.ui.change.setText("Done")
        self.ui.status.setReadOnly(self.changing)
        self.ui.gnf.blockSignals(self.changing)
        self.ui.gay.blockSignals(self.changing)
        self.ui.abuzer.blockSignals(self.changing)
        self.ui.cursed.blockSignals(self.changing)
        self.changing += 1
        self.changing %= 2

    def exitClicked(self):
        self.accept()