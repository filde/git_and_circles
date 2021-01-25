import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5 import uic
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.w = 300
        self.h = 300
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.do_paint = False
        self.setMouseTracking(True)


    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if not self.do_paint:
            return
        qp = QPainter()
        qp.begin(self)
        x, y = randint(5, self.w - 5), randint(5, self.h - 5)
        r = randint(4, min(self.w - x, x, y, self.h - y))
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(QPoint(x, y), r, r)
        qp.end()
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
