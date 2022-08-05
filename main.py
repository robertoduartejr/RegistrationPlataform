from PyQt5 import uic,QtWidgets
import Validators

def window_swap(wopen,wclose):
    wopen.show()
    wclose.close()

#le = QtWidgets.QLineEdit()
#le.setEchoMode(QtWidgets.QLineEdit.Password)

app=QtWidgets.QApplication([])
main_window = uic.loadUi("Tela_Inicial.ui")
login_window = uic.loadUi("Login.ui")
signup_window = uic.loadUi("Cadastro.ui")
edit_window = uic.loadUi("Editar.ui")
dashboard_window = uic.loadUi("Dashboard.ui")
verification_window = uic.loadUi("Verificacao.ui")

cliente_novo = Validators.Validators(signup_window,1,verification_window)
cliente_editar = Validators.Validators(edit_window,0,verification_window)

#report.pushButton.clicked.connect(cliente.Data_Validator)
#instructions for all buttons in all pages
main_window.pushButton.clicked.connect(lambda: window_swap(signup_window,main_window))
main_window.pushButton_2.clicked.connect(lambda: window_swap(login_window,main_window))
signup_window.pushButton_2.clicked.connect(lambda: window_swap(main_window,signup_window))
signup_window.pushButton.clicked.connect(cliente_novo.Data_Validator)
login_window.pushButton_2.clicked.connect(lambda: window_swap(dashboard_window,login_window))
login_window.pushButton_3.clicked.connect(lambda: window_swap(main_window,login_window))
dashboard_window.pushButton.clicked.connect(lambda: window_swap(edit_window,dashboard_window))
edit_window.pushButton_2.clicked.connect(lambda: window_swap(dashboard_window,edit_window))
edit_window.pushButton.clicked.connect(cliente_editar.Data_Validator)

main_window.show()
app.exec()
