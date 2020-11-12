# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MY_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.posx = 400
        self.posy = 500
        self.length = 300
        self.height = 350
        self.title = 'Test'
        self.initUI()

    def initUI(self):
        self.setGeometry(self.posx, self.posy, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        self.key_number_box = QLabel('输入按键', self)
        self.key_number_box.resize(200, 40)
        self.key_number_box.move(50, 100)

    def keyPressEvent(self, event):
        # print(event.key())
        self.key_number_box.setText('当前按键值:' + str(event.key()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my = MY_UI()

    my.show()

    sys.exit(app.exec_())
