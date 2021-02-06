"""

@author: Maxime-Missichini

With this file, we aim to drag & drop labels (in our case, among us characters)

"""
import sys

from PyQt5.QtWidgets import QLabel

import main


def crewPlaceMode(Menu):


    if Menu.crewPlace is False:
        Menu.crewPlace = True
        # Creating one label for one color, we store it in an array because a player can have 12 pins max
        redLabel = QLabel(Menu.mapLabel)
        blueLabel = QLabel(Menu.mapLabel)
        orangeLabel = QLabel(Menu.mapLabel)
        whiteLabel = QLabel(Menu.mapLabel)
        blackLabel = QLabel(Menu.mapLabel)
        cyanLabel = QLabel(Menu.mapLabel)
        yellowLabel = QLabel(Menu.mapLabel)
        pinkLabel = QLabel(Menu.mapLabel)
        purpleLabel = QLabel(Menu.mapLabel)
        limeLabel = QLabel(Menu.mapLabel)
        greenLabel = QLabel(Menu.mapLabel)
        brownLabel = QLabel(Menu.mapLabel)
        Menu.playerPins = [redLabel,blueLabel,orangeLabel,whiteLabel,blackLabel,cyanLabel,yellowLabel,pinkLabel,purpleLabel,
                      limeLabel,greenLabel,brownLabel]
    else:
        Menu.crewPlace = False
        # Temporary
        for widg in Menu.playerPins:
            widg.destroy()
