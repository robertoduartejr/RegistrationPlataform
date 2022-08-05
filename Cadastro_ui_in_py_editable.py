from Cadastro_ui_in_py import *
import sys
import Validators


class SignupWindow(Ui_MainWindow):
    def __init__(self,window,wopen,verification_window):
        print("foi")
        self.window = window
        self.setupUi(window)
        self.pushButton_2.clicked.connect(lambda: self.window_swap(wopen,window))
        self.pushButton.clicked.connect(lambda: self.register_database(self,verification_window))
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)

    def window_swap(self,wopen,wclose):
        wopen.show()
        wclose.close()
    def register_database(self,currentwindow,verification_window):
        cliente_novo = Validators.Validators(currentwindow,1,verification_window)
        cliente_novo.Data_Validator()
        print("function to register in database")


