import datetime
import re
import smtplib
import random

class Validators:
    def __init__(self, report):
        self.report = report
        print("chegou aqui?")

    def emailConfirmation(self,name,email):
        numbers = '0123456789'
        code = ''
        for i in range(6):
            code = code + random.choice(numbers)
        body = f'Subject: Codigo de Verificacao. \nDear ContactName, \n\n' + f' Ola, {name}. \n\n Aqui se encontra seu codigo de verificacao: {code}' + '\n Obrigado, Equipe'
        try:
            smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        except Exception as e:
            print(e)
            smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
        try:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('pessoatestecsv@outlook.com', 'Senhacurso12345')
            smtpObj.sendmail('pessoatestecsv@outlook.com', email, body)  # Or recipient@outlook
            smtpObj.quit()
            self.report.label_24.setText("")
            print(code)
            return True, code
        except Exception as e:
            self.report.label_24.setText("Conexão Falhou")
            return False, 0



    def birthValidation(self,date):
        month, day, year = date.split('/')
        print(month, day, year)
        isValidDate = True
        try:
            d1 = datetime.datetime(int(year), int(month), int(day))
            d2 = datetime.datetime.today()
            if d1 > d2:  # condition to guarentee no one was born in the future
                self.report.label_19.setText("Data Inválida")
                return False
        except ValueError:
            self.report.label_19.setText("Data Inválida")
            return False
        if (isValidDate):
            self.report.label_19.setText("")
            return True

    def passwordValidation(self,password):
        if len(password) < 8:
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

    def passwordConfirmation(self,password, passwordconfirmation):
        if password == passwordconfirmation:
            return True
        else:
            return False

    # function to validate some fields
    def nameValidator(self,name, label):
        if name.replace(" ", "").isalpha():
            label.setText("")
            return True
        else:
            label.setText("Apenas caracteres alfabéticos")
            return False

    def emailValidator(self,email,label):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat, email):
            label.setText("")
            return True
        label.setText("Email Invalido")
        return False


    def cpf_validate(self,numbers):
        #  Obtém os números do CPF e ignora outros caracteres
        cpf = [int(char) for char in numbers if char.isdigit()]

        #  Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            self.report.label_18.setText("CPF Inválido")
            return False

        #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
        #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
        #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
        if cpf == cpf[::-1]:
            self.report.label_18.setText("CPF Inválido")
            return False

        #  Valida os dois dígitos verificadores
        for i in range(9, 11):
            value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpf[i]:
                self.report.label_18.setText("CPF Inválido")
                return False
        self.report.label_18.setText("")
        return True

    def Data_Validator(self):
        print("validator")
        name = self.report.lineEdit.text()
        surname = self.report.lineEdit_2.text()
        cpf = self.report.lineEdit_3.text()
        birth_date = self.report.dateEdit.text()
        city = self.report.lineEdit_4.text()
        uf = self.report.comboBox.currentText()
        profession = self.report.lineEdit_5.text()
        team = self.report.lineEdit_6.text()
        film_category = self.report.lineEdit_7.text()
        to_do_list = self.report.textEdit.toPlainText()
        buy_list = self.report.textEdit_2.toPlainText()
        email = self.report.lineEdit_8.text()
        password = self.report.lineEdit_9.text()
        password_confirmation = self.report.lineEdit_10.text()

        # validators

        name_validator = self.nameValidator(name, self.report.label_3)
        surname_validator = self.nameValidator(surname, self.report.label_17)
        cpf_validator = self.cpf_validate(cpf)
        birth_date_validator = self.birthValidation(birth_date)
        city_validator = self.nameValidator(city, self.report.label_20)
        profession_validator = self.nameValidator(profession, self.report.label_21)
        team_validator = self.nameValidator(team, self.report.label_22)
        film_category_validator = self.nameValidator(film_category, self.report.label_23)
        email_validator = self.emailValidator(email, self.report.label_24)
        password_validator = self.passwordValidation(password)
        password_confirmation_validator = self.passwordConfirmation(password, password_confirmation)

        validation = [name_validator, surname_validator, cpf_validator, birth_date_validator, city_validator,
                      profession_validator, team_validator, film_category_validator, email_validator,
                      password_validator,
                      password_confirmation_validator]

        if False in validation:
            print("nok")
        else:
            password_validator, code = self.emailConfirmation(name, email)
            print(code)