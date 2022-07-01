from PyQt5.QtWidgets import QDialog, QMessageBox
from mysearcher import Ui_Dialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSignal, QObject, qDebug



class Searcher(QDialog):
    def __init__(self, ghouls, parent=None):
        super().__init__(parent)
        self.ghouls = ghouls
        self.selected = ''
        self.chat_name = ''
        self.fine = 0
        self.setupUi(ghouls)

    def closeEvent(self, event):
        if self.fine:
            event.accept()
        else:
            qDebug('very bad')
            event.ignore()

    def setupUi(self, ghouls):
        super(Searcher, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ghoulsmodel = QStandardItemModel()
        self.ui.listView.setModel(self.ghoulsmodel)
        for i in self.ghouls:
            item = QStandardItem(i)
            item.setSelectable(1)
            self.ghoulsmodel.appendRow(item)
        self.ui.create.clicked.connect(self.chat_created)


    def chat_created(self):
        if self.ui.lineEdit.text() == '':
            self.ui.label.setText("Input chat name!")
        else:
            indexes = self.ui.listView.selectedIndexes()
            for i in indexes:
                self.selected += self.ghoulsmodel.itemFromIndex(i).text() + ','
            self.selected += self.ui.lineEdit.text()
            self.fine = 1
            self.close()

