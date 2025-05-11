
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QFileDialog
import os

from pygame import *

from player import Ui_MainWindow as PlayerUI

mixer.init()

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(839, 637)
        self.setStyleSheet("background-color : #2c2c2c;")

        self.label = QtWidgets.QLabel("Login:", self)
        self.label.setGeometry(QtCore.QRect(290, 220, 50, 20))
        self.label.setStyleSheet("color: white;")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setStyleSheet("color: white;")
        self.lineEdit.setGeometry(QtCore.QRect(350, 220, 150, 20))

        self.label_2 = QtWidgets.QLabel("Password:", self)
        self.label_2.setGeometry(QtCore.QRect(290, 260, 60, 20))
        self.label_2.setStyleSheet("color: white;")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setStyleSheet("color: white;")
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 260, 150, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)


        self.pushButton = QtWidgets.QPushButton("Sign in", self)
        self.pushButton.setGeometry(QtCore.QRect(350, 300, 150, 50))
        self.pushButton.setStyleSheet("background-color: #563C5C; color: white; font-size: 24px;")
        self.pushButton.clicked.connect(self.login)

        self.player = QMediaPlayer()
        self.folder_path = ''

    def login(self):
        login_text = self.lineEdit.text()
        password_text = self.lineEdit_2.text()

        if login_text == "bogdan" and password_text == "spoticharm":
            self.open_player()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid login or password")










    def open_player(self):
        self.player_window = QtWidgets.QMainWindow()
        self.player_ui = PlayerUI()
        self.player_ui.setupUi(self.player_window)
        self.player_ui.pushButton_6.clicked.connect(self.showFilenamesList)
        self.player_ui.pushButton_3.clicked.connect(self.playChosenSong)
        self.player_ui.pushButton_3.setText("▶️")
        self.player_ui.pushButton_2.clicked.connect(self.playNextSong)
        self.player_ui.pushButton.clicked.connect(self.playPreviousSong)
        self.player_ui.pushButton_5.clicked.connect(self.skipForward10Seconds)
        self.player_ui.pushButton_4.clicked.connect(self.backForward10Seconds)

        self.player_window.show()
        self.close()

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Вибрати папку")


    def filter(self, files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result


    def showFilenamesList(self):
        extensions = ['.mp3']
        self.folder_path = QFileDialog.getExistingDirectory(self, "Вибрати папку")
        filenames = self.filter(os.listdir(self.folder_path), extensions)

        self.player_ui.listWidget.clear()
        for filename in filenames:
            self.player_ui.listWidget.addItem(filename)
        print(filenames)

    def playSong(self):
        if self.player_ui.listWidget.currentRow() >= 0:
            filename = self.player_ui.listWidget.currentItem().text()
            full_path = os.path.join(self.folder_path, filename)

            if not os.path.exists(full_path):
                print("Файл не найден:", full_path)
                return

            url = QUrl.fromLocalFile(full_path)
            content = QMediaContent(url)
            self.player.setMedia(content)
            self.player.play()
            self.player_ui.pushButton_3.setText("⏸️")  # Воспроизведение началось


    def playChosenSong(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.player_ui.pushButton_3.setText("▶️")  # Кнопка: воспроизведение
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
            self.player_ui.pushButton_3.setText("⏸️")  # Кнопка: пауза
        else:
            self.playSong()

    #lw_files.currentRowChanged.connect(showChosenImage)

    def playNextSong(self):
        current_row = self.player_ui.listWidget.currentRow()
        total_items = self.player_ui.listWidget.count()

        if current_row < total_items - 1:  # Проверяем, не последний ли элемент
            next_row = current_row + 1
            self.player_ui.listWidget.setCurrentRow(next_row)
            self.playSong()


    def playPreviousSong(self):
        current_row = self.player_ui.listWidget.currentRow()
        total_items = self.player_ui.listWidget.count()

        if current_row != 0:
            next_row = current_row - 1
            self.player_ui.listWidget.setCurrentRow(next_row)
            self.playSong()
        else:
            print("Это была first песня.")

    def skipForward10Seconds(self):
        current_position = self.player.position()
        new_position = current_position + 10000  # 10 секунд = 10000 миллисекунд
        duration = self.player.duration()

        if new_position < duration:
            self.player.setPosition(new_position)
            print(f"Перемотано на 10 секунд вперёд: {new_position} мс")
        else:
            self.player.setPosition(duration)
            print("Перемотано до конца трека.")

    def backForward10Seconds(self):
        current_position = self.player.position()
        new_position = current_position - 10000  # 10 секунд = 10000 миллисекунд
        duration = self.player.duration()

        if new_position < duration:
            self.player.setPosition(new_position)
            print(f"Перемотано на 10 секунд back: {new_position} мс")
        else:
            self.player.setPosition(duration)
            print("Перемотано до start трека.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
