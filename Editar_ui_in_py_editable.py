from Editar_ui_in_py import *
import sys
import Validators

#class to edit and set password as blind for Cadastro

class EditWindow(Ui_MainWindow):
    def __init__(self,window):
        print("foi msm?")
        self.window = window
        self.setupUi(window)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)
