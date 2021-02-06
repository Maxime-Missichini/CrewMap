import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap

import main
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLayout, QHBoxLayout, QMainWindow, QGroupBox


class ChooseMap(QMainWindow):

    def __init__(self,Menu):
        super().__init__()

        self.buttonBox = QGroupBox(self)
        self.layout = QHBoxLayout(self.buttonBox)
        self.done = False

        self.skeld = QPushButton("Skeld",self)
        self.skeld.clicked.connect(lambda: self.pickSkeld(Menu))

        self.mira = QPushButton("Mira",self)
        self.mira.clicked.connect(lambda: self.pickMira(Menu))

        self.polus = QPushButton("Polus",self)
        self.polus.clicked.connect(lambda: self.pickPolus(Menu))

        self.buttonBox.setGeometry(QRect(0, 0, 500, 100))
        self.layout.addWidget(self.skeld)
        self.layout.addWidget(self.mira)
        self.layout.addWidget(self.polus)
        self.setLayout(self.layout)

        self.setWindowTitle("Choose a map")
        self.setGeometry(QRect(0,0,510,110))
        self.setFixedSize(510,110)

        self.show()

    def pickSkeld(self,Menu):
        image = QPixmap("./assets/maps/skeld.png")
        self.done = True
        Menu.map = image.scaled(1200, 1200, Qt.KeepAspectRatio, Qt.FastTransformation)

    def pickMira(self,Menu):
        image = QPixmap("./assets/maps/mira.png")
        self.done = True
        Menu.map = image.scaled(1200, 1200, Qt.KeepAspectRatio, Qt.FastTransformation)

    def pickPolus(self,Menu):
        image = QPixmap("./assets/maps/polus.png")
        self.done = True
        Menu.map = image.scaled(1200, 1200, Qt.KeepAspectRatio, Qt.FastTransformation)