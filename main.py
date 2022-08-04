from PyQt5 import uic,QtWidgets
import Validators


app=QtWidgets.QApplication([])
report = uic.loadUi("Tela_Inical.ui")

cliente = Validators.Validators(report)

report.pushButton.clicked.connect(cliente.Data_Validator)

report.show()
app.exec()