from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from mysearcher import Ui_Dialog
from PyQt5.QtCore import pyqtSignal, QObject


class Searcher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        super(Searcher, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
