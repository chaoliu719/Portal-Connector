from sys import argv, exit

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QStandardItemModel, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QGroupBox, QLabel, QTreeView, QWidget
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QLineEdit

from core import connect_portal, test_public
from Qss import *


class MainWindow(QWidget):
    Id, Password = range(2)
    CONFIG_FILE = 'config'

    def __init__(self):
        super().__init__()
        with open(self.CONFIG_FILE, 'a'):
            pass
        self.init()

    def init(self):
        # ------ initUI
        self.resize(555, 245)
        self.setFixedSize(555, 245)
        self.center()
        self.setWindowTitle('Portal Connector')
        self.setWindowIcon(QIcon('gao.ico'))
        self.backgroundRole()
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(250, 250, 250))   # 设置背景颜色

        self.setPalette(palette1)

        # ------setLeftWidget

        self.dataGroupBox = QGroupBox("Saved", self)
        self.dataGroupBox.setGeometry(10, 10, 60, 20)
        self.dataGroupBox.setStyleSheet(MyGroupBox)

        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.Id, Qt.Horizontal, "Id")
        self.model.setHeaderData(self.Password, Qt.Horizontal, "Pw")

        self.dataView = QTreeView(self)
        self.dataView.setGeometry(10, 32, 255, 150)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
        self.dataView.setModel(self.model)
        self.dataView.setStyleSheet(MyTreeView)

        save_btn = QPushButton('Save', self)
        save_btn.setGeometry(15, 195, 100, 35)
        save_btn.setStyleSheet(MyPushButton)

        delete_btn = QPushButton('Delete', self)
        delete_btn.setGeometry(135, 195, 100, 35)
        delete_btn.setStyleSheet(MyPushButton)

        # ------ setRightWidget

        username = QLabel('Id:', self)
        username.setGeometry(300, 45, 50, 30)
        username.setStyleSheet(MyLabel)

        self.username_edit = QLineEdit(self)
        self.username_edit.setGeometry(350, 40, 190, 35)
        self.username_edit.setStyleSheet(MyLineEdit)

        password = QLabel('Pw:', self)
        password.setGeometry(300, 100, 50, 30)
        password.setStyleSheet(MyLabel)

        self.password_edit = QLineEdit(self)
        self.password_edit.setGeometry(350, 95, 190, 35)
        self.password_edit.setStyleSheet(MyLineEdit)

        status_label = QLabel('Result:', self)
        status_label.setGeometry(295, 150, 70, 30)
        status_label.setStyleSheet(UnderLabel)

        self.status = QLabel('Disconnect', self)
        self.status.setGeometry(360, 150, 190, 30)
        self.status.setStyleSheet(UnderLabel)

        connect_btn = QPushButton('Connect', self)
        connect_btn.setGeometry(320, 195, 100, 35)
        connect_btn.setStyleSheet(MyPushButton)

        test_btn = QPushButton('Test', self)
        test_btn.setGeometry(440, 195, 100, 35)
        test_btn.setStyleSheet(MyPushButton)

        # ------setTabOrder

        self.setTabOrder(self.username_edit, self.password_edit)
        self.setTabOrder(self.password_edit, connect_btn)
        self.setTabOrder(connect_btn, test_btn)

        # ------setEvent

        self.dataView.mouseDoubleClickEvent = self.set_text
        self.dataView.mousePressEvent = self.set_focus
        delete_btn.clicked.connect(self.removeItem)
        connect_btn.clicked.connect(self.connect_clicked)
        save_btn.clicked.connect(self.save_infomation)
        test_btn.clicked.connect(self.test_network)

        self.readItem(self.CONFIG_FILE)
        self.connect_clicked()
        self.show()

    def connect_clicked(self):
        result = connect_portal(self.username_edit.text(), self.password_edit.text())
        self.status.setText(result)

    def save_infomation(self):
        if self.username_edit.text() and self.password_edit.text():
            try:
                selected = self.dataView.selectedIndexes()[0].row()
                self.modifyItem(selected)
            except IndexError:
                self.addItem(self.username_edit.text(), self.password_edit.text())

    def test_network(self):
        result = test_public()
        self.status.setText(result)

    def set_text(self, event=None):
        try:
            self.username_edit.setText(self.dataView.selectedIndexes()[0].data())
            self.password_edit.setText(self.dataView.selectedIndexes()[1].data())
        except IndexError:
            pass

    def set_focus(self, event):
        index = self.dataView.indexAt(event.pos())
        if not index.isValid():
            self.dataView.clearSelection()
        else:
            self.dataView.setCurrentIndex(index)

    def readItem(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.addItem(*(line.split()))

        self.dataView.setCurrentIndex(self.dataView.indexAt(QPoint(1, 1)))
        self.set_text()

    def addItem(self, username, password):
        self.model.insertRow(0)
        self.model.setData(self.model.index(0, self.Id), username)
        self.model.setData(self.model.index(0, self.Password), password)
        self.save_to_file()

    def modifyItem(self, row):
        self.model.setData(self.model.index(row, self.Id), self.username_edit.text())
        self.model.setData(self.model.index(row, self.Password), self.password_edit.text())
        self.save_to_file()

    def removeItem(self):
        try:
            self.model.removeRow(self.dataView.selectedIndexes()[0].row())
            self.save_to_file()
        except IndexError:
            pass

    def save_to_file(self):
        with open(self.CONFIG_FILE, 'w') as f:
            for x in range(self.model.rowCount()):
                for y in range(self.model.columnCount()):
                    f.write(self.model.data(self.model.index(x, y)) + " ")
                f.write("\n")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MainWindow()
    exit(app.exec_())
