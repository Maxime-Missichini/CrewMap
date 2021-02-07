"""

@author: Maxime-Missichini

"""
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QFrame, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor


def crewPlaceMode(Menu):

    if Menu.crewPlace is False:
        Menu.crewPlace = True
        Menu.stateLabel.setText("Place Crewmate mode")
        # Creating one label for each color, we store it in an array because a player can have 12 pins max
        redLabel = QLabel(Menu)
        redLabel.setGeometry(0,0,100,100)
        redLabel.setPixmap(QPixmap("./assets/crewmates/red.png"))

        blueLabel = QLabel(Menu)
        blueLabel.setGeometry(QRect(0,0,0, 0))
        blueLabel.setPixmap(QPixmap("./assets/crewmates/blue.png"))

        orangeLabel = QLabel(Menu)
        orangeLabel.setGeometry(QRect(0, 0, 0, 0))
        orangeLabel.setPixmap(QPixmap("./assets/crewmates/orange.png"))

        whiteLabel = QLabel(Menu)
        whiteLabel.setGeometry(QRect(0, 0, 0, 0))
        whiteLabel.setPixmap(QPixmap("./assets/crewmates/white.png"))

        blackLabel = QLabel(Menu)
        blackLabel.setGeometry(QRect(0, 0, 0, 0))
        blackLabel.setPixmap(QPixmap("./assets/crewmates/black.png"))

        cyanLabel = QLabel(Menu)
        cyanLabel.setGeometry(QRect(0, 0, 0, 0))
        cyanLabel.setPixmap(QPixmap("./assets/crewmates/cyan.png"))

        yellowLabel = QLabel(Menu)
        yellowLabel.setGeometry(QRect(0, 0, 0, 0))
        yellowLabel.setPixmap(QPixmap("./assets/crewmates/yellow.png"))

        pinkLabel = QLabel(Menu)
        pinkLabel.setGeometry(QRect(0, 0, 0, 0))
        pinkLabel.setPixmap(QPixmap("./assets/crewmates/pink.png"))

        purpleLabel = QLabel(Menu)
        purpleLabel.setGeometry(QRect(0, 0, 0, 0))
        purpleLabel.setPixmap(QPixmap("./assets/crewmates/purple.png"))

        limeLabel = QLabel(Menu)
        limeLabel.setGeometry(QRect(0, 0, 0, 0))
        limeLabel.setPixmap(QPixmap("./assets/crewmates/lime.png"))

        greenLabel = QLabel(Menu)
        greenLabel.setGeometry(QRect(0, 0, 0, 0))
        greenLabel.setPixmap(QPixmap("./assets/crewmates/green.png"))

        brownLabel = QLabel(Menu)
        brownLabel.setGeometry(QRect(0, 0, 0, 0))
        brownLabel.setPixmap(QPixmap("./assets/crewmates/brown.png"))

        Menu.playerPins = [redLabel,blueLabel,orangeLabel,whiteLabel,blackLabel,cyanLabel,yellowLabel,pinkLabel,purpleLabel,
                      limeLabel,greenLabel,brownLabel]

        Menu.labelToMove = Menu.playerPins[0]
        newCrewPixMap = Menu.labelToMove.pixmap().scaled(50,50, Qt.KeepAspectRatio, Qt.FastTransformation)
        Menu.labelToMove.setPixmap(newCrewPixMap)

    else:
        Menu.crewPlace = False
        Menu.stateLabel.setText("Draw mode")


def changeCrewColor(Menu):
    # choosing the right image
    index = 0
    i = 0
    for col in Menu.colorList:
        if col == Menu.currentColor:
            index = i
        else:
            i += 1
    Menu.labelToMove = Menu.playerPins[index]
    newCrewPixMap = Menu.labelToMove.pixmap().scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
    Menu.labelToMove.setPixmap(newCrewPixMap)