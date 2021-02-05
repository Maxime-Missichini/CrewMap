import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QFrame, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()  # super to main window
        self.drawing = False
        self.lastPoint = QPoint()
        self.frameButtons = QFrame()

        #Map image
        self.mapLabel = QtWidgets.QLabel()
        oldimage = QPixmap("C:/Users/Themy/Desktop/pythonProject3/skeld_map.png")
        image = oldimage.scaled(800,800,Qt.KeepAspectRatio,Qt.FastTransformation)
        self.mapLabel.setPixmap(image)

        #Buttons
        self.buttonBox = QGroupBox(self)
        self.colorLayout = QHBoxLayout(self.buttonBox)
        redSelector = QPushButton(self.buttonBox)
        redSelector.setStyleSheet("background-color: red")
        redSelector.clicked.connect(lambda: self.changeColor(Qt.red))
        blueSelector = QPushButton(self.buttonBox)
        blueSelector.setStyleSheet("background-color: blue")
        blueSelector.clicked.connect(lambda: self.changeColor(Qt.blue))
        orangeSelector = QPushButton(self.buttonBox)
        orangeSelector.setStyleSheet("background-color: orange")
        orangeSelector.clicked.connect(lambda: self.changeColor(QColor(255,165,0)))
        whiteSelector = QPushButton(self.buttonBox)
        whiteSelector.setStyleSheet("background-color: white")
        whiteSelector.clicked.connect(lambda: self.changeColor(QColor(255,255,255)))
        blackSelector = QPushButton(self.buttonBox)
        blackSelector.setStyleSheet("background-color: black")
        blackSelector.clicked.connect(lambda: self.changeColor(Qt.black))
        cyanSelector = QPushButton(self.buttonBox)
        cyanSelector.setStyleSheet("background-color: cyan")
        cyanSelector.clicked.connect(lambda: self.changeColor(QColor(0,255,255)))
        yellowSelector = QPushButton(self.buttonBox)
        yellowSelector.setStyleSheet("background-color: yellow")
        yellowSelector.clicked.connect(lambda: self.changeColor(Qt.yellow))
        pinkSelector = QPushButton(self.buttonBox)
        pinkSelector.setStyleSheet("background-color: pink")
        pinkSelector.clicked.connect(lambda: self.changeColor(QColor(255,192,203)))
        purpleSelector = QPushButton(self.buttonBox)
        purpleSelector.setStyleSheet("background-color: purple")
        purpleSelector.clicked.connect(lambda: self.changeColor(QColor(128,0,128)))
        limeSelector = QPushButton(self.buttonBox)
        limeSelector.setStyleSheet("background-color: lime")
        limeSelector.clicked.connect(lambda: self.changeColor(QColor(0,255,0)))
        greenSelector = QPushButton(self.buttonBox)
        greenSelector.setStyleSheet("background-color: green")
        greenSelector.clicked.connect(lambda: self.changeColor(QColor(0,128,0)))
        brownSelector = QPushButton(self.buttonBox)
        brownSelector.setStyleSheet("background-color: brown")
        brownSelector.clicked.connect(lambda: self.changeColor(QColor(165,42,42)))
        self.colorLayout.addWidget(redSelector)
        self.colorLayout.addWidget(blueSelector)
        self.colorLayout.addWidget(orangeSelector)
        self.colorLayout.addWidget(whiteSelector)
        self.colorLayout.addWidget(blackSelector)
        self.colorLayout.addWidget(cyanSelector)
        self.colorLayout.addWidget(yellowSelector)
        self.colorLayout.addWidget(pinkSelector)
        self.colorLayout.addWidget(purpleSelector)
        self.colorLayout.addWidget(limeSelector)
        self.colorLayout.addWidget(greenSelector)
        self.colorLayout.addWidget(brownSelector)

        self.buttonBox.setGeometry(QRect(0,self.mapLabel.pixmap().height(),self.mapLabel.pixmap().width(),50))



        #Window settings
        self.setGeometry(QRect(0,0,self.mapLabel.pixmap().width(),self.mapLabel.pixmap().height()+100))
        self.show()

    def changeColor(self, color):
        self.currentColor = color

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
            if self.currentColor is None:
                painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.setPen(QPen(self.currentColor, 3, Qt.SolidLine))
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
