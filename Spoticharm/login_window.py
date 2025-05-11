from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import pygame
from pygame import mixer
from player import Ui_MainWindow as PlayerUI

pygame.mixer.init()
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(839, 637)
        self.setStyleSheet("background-color : #2c2c2c;")
        self.current_index = 0
        self.filenames = []
        self.folder_path = ''