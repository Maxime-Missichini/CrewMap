import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QFrame
from PyQt5.QtGui import QPixmap, QPainter, QPen


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()  # super to main window
        self.drawing = False
        self.lastPoint = QPoint()

        self.frameButtons = QFrame()

        self.mapLabel = QtWidgets.QLabel()
        image = QPixmap("C:/Users/Themy/Desktop/pythonProject3/skeld_map.png")
        self.mapLabel.setPixmap(image)

        self.colorSelector = QPushButton("Color")
        self.frameButtons.drawFrame()

        self.setGeometry(100, 100, 1500, 800)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.mapLabel.pixmap().rect(), self.mapLabel.pixmap())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.mapLabel.pixmap())
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    sys.exit(app.exec_())
