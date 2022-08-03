from PyQt5 import uic,QtWidgets
import datetime

def birthValidation(date):
    month,day,year = date.split('/')
    print(month,day,year)
    isValidDate = True
    try :
        d1 = datetime.datetime(int(year), int(month), int(day))
        d2 = datetime.datetime.today()
        if d1>d2: #condition to guarentee no one was born in the future
           return False
    except ValueError :
        return False
    if(isValidDate) :
        return True

def passwordValidation(password):
    if len(password)<8:
        print("entrou1")
        return False
    if password.islower():
        print("entrou1")
        return False
    if password.isupper():
        print("entrou1")
        return False
    if password.isalpha():
        print("entrou2")
        return False
    if password.isalnum():
        print("entrou3")
        return False
    else:
        print("retornou bom")
        return True

def passwordConfirmation(password,passwordconfirmation):
    if password == passwordconfirmation:
        return True
    else:
        return False

#function to validate some fields
def nameValidator(name):
    if name.replace(" ", "").isalpha():
        return True
    else:
        return False

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

#function to register information on SQL
def register_function():
    print("testt")

#function to call all validators
def Data_Validator():
    print("validator")
    name = report.lineEdit.text()
    surname = report.lineEdit_2.text()
    cpf = report.lineEdit_3.text()
    birth_date = report.dateEdit.text()
    city = report.lineEdit_4.text()
    uf = report.comboBox.currentText()
    profession = report.lineEdit_5.text()
    team = report.lineEdit_6.text()
    film_category = report.lineEdit_7.text()
    to_do_list = report.textEdit.toPlainText()
    buy_list = report.textEdit_2.toPlainText()
    email = report.lineEdit_8.text()
    password = report.lineEdit_9.text()
    password_confirmation = report.lineEdit_10.text()

    #validators
    name_validator = False
    surname_validator = False
    cpf_validator = False
    birth_date_validator = False
    city_validator = False
    profession_validator = False
    team_validator = False
    film_category_validator = False
    email_validator = False
    password_validator = False
    password_confirmation_validator = False


    print("aqui")
    name_validator = nameValidator(name)
    surname_validator = nameValidator(surname)
    cpf_validator = cpf_validate(cpf)
    birth_date_validator = birthValidation(birth_date)
    city_validator = nameValidator(city)
    profession_validator = nameValidator(profession)
    team_validator = nameValidator(team)
    film_category_validator = nameValidator(film_category)
    email_validator = nameValidator(email)
    password_validator = passwordValidation(password)
    password_confirmation_validator = passwordConfirmation(password,password_confirmation)


    validation = [name_validator, surname_validator, cpf_validator, birth_date_validator, city_validator,
                  profession_validator, team_validator, film_category_validator, email_validator, password_validator,
                  password_confirmation_validator]

    for x in validation:
        print(x)

app=QtWidgets.QApplication([])
report = uic.loadUi("Tela_Inical.ui")


report.pushButton.clicked.connect(Data_Validator)

report.show()
app.exec()