from Cadastro_ui_in_py import *
import sys
import Validators

#class to edit and set password as blind for Cadastro

class SignupWindow(Ui_MainWindow):
    def __init__(self,window):
        self.window = window
        self.setupUi(window)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)



