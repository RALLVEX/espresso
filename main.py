import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
import sqlite3
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        con = sqlite3.connect("coffee.sqlite")
        uic.loadUi('main.ui', self)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())