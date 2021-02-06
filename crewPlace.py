"""

@author: Maxime-Missichini

With this file, we aim to drag & drop labels (in our case, among us characters)

"""
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QFrame, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor

import main



def crewPlaceMode(Menu):

    if Menu.crewPlace is False:
        Menu.crewPlace = True

        # Creating one label for each color, we store it in an array because a player can have 12 pins max
        redLabel = QLabel(Menu)
        redLabel.setGeometry(0,0,100,100)
        blueLabel = QLabel(Menu)
        blueLabel.setGeometry(QRect(0,0,0, 0))
        orangeLabel = QLabel(Menu)
        orangeLabel.setGeometry(QRect(0, 0, 0, 0))
        whiteLabel = QLabel(Menu)
        whiteLabel.setGeometry(QRect(0, 0, 0, 0))
        blackLabel = QLabel(Menu)
        blackLabel.setGeometry(QRect(0, 0, 0, 0))
        cyanLabel = QLabel(Menu)
        cyanLabel.setGeometry(QRect(0, 0, 0, 0))
        yellowLabel = QLabel(Menu)
        yellowLabel.setGeometry(QRect(0, 0, 0, 0))
        pinkLabel = QLabel(Menu)
        pinkLabel.setGeometry(QRect(0, 0, 0, 0))
        purpleLabel = QLabel(Menu)
        purpleLabel.setGeometry(QRect(0, 0, 0, 0))
        limeLabel = QLabel(Menu)
        limeLabel.setGeometry(QRect(0, 0, 0, 0))
        greenLabel = QLabel(Menu)
        greenLabel.setGeometry(QRect(0, 0, 0, 0))
        brownLabel = QLabel(Menu)
        brownLabel.setGeometry(QRect(0, 0, 0, 0))
        Menu.playerPins = [redLabel,blueLabel,orangeLabel,whiteLabel,blackLabel,cyanLabel,yellowLabel,pinkLabel,purpleLabel,
                      limeLabel,greenLabel,brownLabel]

        # choosing the right image
        index = 0
        i = 0
        for color in Menu.colorList:
            if color is Menu.currentColor:
                index = i
            else:
                i += 1

        Menu.labelToMove = Menu.playerPins[index]
        crewPixmap = QPixmap("./crewmate.png")
        newCrewPixMap = crewPixmap.scaled(50,50, Qt.KeepAspectRatio, Qt.FastTransformation)
        Menu.labelToMove.setPixmap(newCrewPixMap)

    else:
        Menu.crewPlace = False
        # Temporary
        for widg in Menu.playerPins:
            widg.destroy()

def changeCrewColor(Menu):
    # choosing the right image
    index = 0
    i = 0
    for color in Menu.colorList:
        if color is Menu.currentColor:
            index = i
        else:
            i += 1
    print(index)
    Menu.labelToMove = Menu.playerPins[index]
    crewPixmap = QPixmap("./crewmate.png")
    newCrewPixMap = crewPixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
    Menu.labelToMove.setPixmap(newCrewPixMap)