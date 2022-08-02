from PyQt5 import uic,QtWidgets

def register_function():
    print("testt")


app=QtWidgets.QApplication([])
report = uic.loadUi("Tela_Inical.ui")
report.pushButton.clicked.connect(register_function)

report.show()
app.exec()