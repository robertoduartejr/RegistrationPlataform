from Testearquivo import *
import sys
class SignupWindow(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickMe)

    def clickMe(self):
        wopen.show()
        wclose.close()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = SignupWindow(MainWindow)

MainWindow.show()
app.exec_()