import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint, QPointF
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(50, 320, 200, 50))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Git и жёлтые окружности"))
        self.btn.setText(_translate("Form", "Нарисовать окружность"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.w = self.h = 300
        self.setupUi(self)
        self.btn.clicked.connect(self.run)
        self.do_paint = False

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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
