from PyQt5 import uic,QtWidgets,QtGui, QtCore
import Validators
import Cadastro_ui_in_py_editable

def window_swap(wopen,wclose):
    wopen.show()
    wclose.close()

app=QtWidgets.QApplication([])
main_window = uic.loadUi("Tela_Inicial.ui")
login_window = uic.loadUi("Login.ui")
edit_window = uic.loadUi("Editar.ui")
dashboard_window = uic.loadUi("Dashboard.ui")
verification_window = uic.loadUi("Verificacao.ui")


#Sign_up window had to rise in a different way, because I need to change password field
SignUp_Window = QtWidgets.QMainWindow()
ui_signup = Cadastro_ui_in_py_editable.SignupWindow(SignUp_Window,main_window,verification_window) #here it calls the window and all buttons for that one
ui_signup.pushButton_2.clicked.connect(lambda: window_swap(main_window,SignUp_Window)) #era so ter entendido que isso funciona271 que eu teria economizado 10h

#cliente_novo = Validators.Validators(signup_window,1,verification_window)
cliente_editar = Validators.Validators(edit_window,0,verification_window)

#report.pushButton.clicked.connect(cliente.Data_Validator)
#instructions for all buttons in all pages
main_window.pushButton.clicked.connect(lambda: window_swap(SignUp_Window,main_window))
main_window.pushButton_2.clicked.connect(lambda: window_swap(login_window,main_window))

login_window.pushButton_2.clicked.connect(lambda: window_swap(dashboard_window,login_window))
login_window.pushButton_3.clicked.connect(lambda: window_swap(main_window,login_window))
dashboard_window.pushButton.clicked.connect(lambda: window_swap(edit_window,dashboard_window))
edit_window.pushButton_2.clicked.connect(lambda: window_swap(dashboard_window,edit_window))
edit_window.pushButton.clicked.connect(cliente_editar.Data_Validator)

main_window.show()
app.exec()
