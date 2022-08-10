from PyQt5 import uic,QtWidgets,QtGui, QtCore
import Validators
import Cadastro_ui_in_py_editable
import Editar_ui_in_py_editable
import Login_ui_in_py_editable
import pyodbc
from Cadastro_ui_in_py import *
import SQL_Integration


def window_swap(wopen,wclose):
    print("teste10")
    wopen.show()
    wclose.close()

#starting database
user_connection = SQL_Integration.SQL_Integration()
connection = user_connection.data_connection()
#user_connection.writedown_edit(connection,'Yana','Duarte','04228772129','01/27/1993','Brasilia','DF','engenheiro','Vasco','action','bla bla bla', 'bla bla bla','Teste12345')


app=QtWidgets.QApplication([])
main_window = uic.loadUi("Tela_Inicial.ui")
dashboard_window = uic.loadUi("Dashboard.ui")
verification_window = uic.loadUi("Verificacao.ui")
Login_Window = QtWidgets.QMainWindow()
SignUp_Window = QtWidgets.QMainWindow()
Edit_Window = QtWidgets.QMainWindow()

#Sign_up window had to rise in a different way, because I need to change password field
#I used a different way for the sign up part. Instead of set the function in this file, I set the function and button activies on Cadastro_ui_in_py_editable

ui_signup = Cadastro_ui_in_py_editable.SignupWindow(SignUp_Window)
ui_signup.pushButton_2.clicked.connect(lambda: window_swap(main_window,SignUp_Window))
cliente_signup = Validators.Validators(ui_signup,1,verification_window,Login_Window,SignUp_Window,user_connection,connection)
ui_signup.pushButton.clicked.connect(cliente_signup.Data_Validator)

#Edit window had to rise in a different way, because I need to change password field

ui_edit = Editar_ui_in_py_editable.EditWindow(Edit_Window) #here it calls the window and all buttons for that one
ui_edit.pushButton_2.clicked.connect(lambda: window_swap(dashboard_window,Edit_Window)) #era so ter entendido que isso funciona271 que eu teria economizado 10h
cliente_editar = Validators.Validators(ui_edit,0,verification_window,dashboard_window,Edit_Window,user_connection,connection)
ui_edit.pushButton.clicked.connect(cliente_editar.Data_Validator)

#Login window had to rise in a different way, because I need to change password field

ui_login = Login_ui_in_py_editable.LoginWindow(Login_Window) #here it calls the window and all buttons for that one
cliente_login = Validators.Validators(ui_login,2,verification_window,dashboard_window,Login_Window,user_connection,connection)
ui_login.pushButton_2.clicked.connect(cliente_login.passwordValidator) #era so ter entendido que isso funciona271 que eu teria economizado 10h
ui_login.pushButton_3.clicked.connect(lambda: window_swap(main_window,Login_Window))

#instructions for the rest of the buttons in all pages
main_window.pushButton.clicked.connect(lambda: window_swap(SignUp_Window,main_window))
main_window.pushButton_2.clicked.connect(lambda: window_swap(Login_Window,main_window))
dashboard_window.pushButton.clicked.connect(lambda: window_swap(Edit_Window,dashboard_window))
dashboard_window.pushButton.clicked.connect(lambda: user_connection.allUserInformation(connection,ui_login.lineEdit_8.text(),ui_edit)) #function to open data on database


main_window.show()


app.exec()
