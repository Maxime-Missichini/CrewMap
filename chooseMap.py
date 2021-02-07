from PyQt5.QtCore import QRect, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLayout, QHBoxLayout, QMainWindow, QGroupBox


class ChooseMap(QMainWindow):

    # Signals should be outside the def like this
    done = pyqtSignal()

    def __init__(self,Menu):
        super().__init__()

        self.done.connect(Menu.loop.quit)

        self.buttonBox = QGroupBox(self)
        self.layout = QHBoxLayout(self.buttonBox)

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
        Menu.map = image
        self.done.emit()
        self.close()

    def pickMira(self,Menu):
        image = QPixmap("./assets/maps/mira.png")
        Menu.map = image
        self.done.emit()
        self.close()

    def pickPolus(self,Menu):
        image = QPixmap("./assets/maps/polus.png")
        Menu.map = image
        self.done.emit()
        self.close()