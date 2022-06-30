import sys
from PyQt5.QtCore import QAbstractTableModel, QModelIndex
from PyQt5.QtCore import Qt


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def index(self, row, column):
            return QModelIndex()

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 2

    def setData(self, index, value, role):
        if role == Qt.DisplayRole:
            self._data[index.row()][index.column()] = value
            return 1
        return 0

