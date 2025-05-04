from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

from player import Ui_MainWindow as PlayerUI


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
        folder_path = ''

    def login(self):
        login_text = self.lineEdit.text()
        password_text = self.lineEdit_2.text()

        if login_text == "admin" and password_text == "123":
            self.open_player()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid login or password")

    def open_player(self):
        self.player_window = QtWidgets.QMainWindow()
        self.player_ui = PlayerUI()
        self.player_ui.setupUi(self.player_window)
        self.player_ui.pushButton_6.clicked.connect(self.showFilenamesList)
        self.player_window.show()
        self.close()



    def filter(self, files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def showFilenamesList(self):
        options = QFileDialog.Options()
        file_filter = "MP3 files (*.mp3);;All files (*)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Вибрати MP3 файл", "", file_filter, options=options)

        if file_path:
            filename = os.path.basename(file_path)
            self.player_ui.listWidget.clear()
            self.player_ui.listWidget.addItem(filename)
            print(filename)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
