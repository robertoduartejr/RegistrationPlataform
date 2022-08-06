import datetime
import re
import smtplib
import random

class Validators:
    def __init__(self, report, comparative,verification,wopen,wclose):
        self.report = report
        print("criei o primeiro self")
        self.comparative = comparative #separate if it`s a validation to sgin up or to edit
        self.verification = verification
        self.wopen = wopen
        self.wclose = wclose
        print("chegou aqui?")

    def window_swap(self,wopen, wclose):
        print("teste10")
        wopen.show()
        wclose.close()

    def emailConfirmation(self,name,email):
        numbers = '0123456789'
        code = ''
        for i in range(6):
            code = code + random.choice(numbers)
        print(code)
        body = f'Subject: Codigo de Verificacao. \nDear ContactName, \n\n' + f' Ola, {name}. \n\n Aqui se encontra seu codigo de verificacao: {code}' + '\n Obrigado, Equipe'
        try:
            smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        except Exception as e:
            print(e)
            smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
        try:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('csvagateste123@outlook.com', 'Senhacurso12345')
            print("ok1")
            smtpObj.sendmail('csvagateste123@outlook.com', email, body)  # Or recipient@outlook
            print("ok2")
            smtpObj.quit()
            self.report.label_24.setText("")
            print(code)
            return True, code
        except Exception as e:
            self.report.label_24.setText("Conexão Falhou")
            return False, code

    def compare_Code(self,code):
        if code == self.verification.lineEdit.text():
            print("Deu bom, chamar função pra por no banco de dados")
            self.verification.close()
            self.window_swap(self.wopen, self.wclose) # troca de janela
        else:
            print("deu erro")
            print("codigo que peguei ",self.verification.lineEdit.text(), "codigo gerado ", code)


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
        for n in password:
            if n == " ":
                self.report.label_25.setText("Não pode conter espaço")
                return False
        if password == "":
            self.report.label_25.setText("Senha em branco")
            return False
        if len(password) < 8:
            self.report.label_25.setText("Senha precisa ter 8 digitos ou mais")
            return False
        if password.islower():
            self.report.label_25.setText("Senha precisa ter pelo menos uma letra maiúscula")
            return False
        if password.isupper():
            self.report.label_25.setText("Senha precisa ter pelo menos uma letra minuscula")
            return False
        if password.isalpha():
            self.report.label_25.setText("Senha precisa ter pelo menos um numero")
            return False
        if password.isalnum():
            self.report.label_25.setText("Senha precisa ter pelo menos um caractere especial")
            return False
        else:
            self.report.label_25.setText("")
            return True

    def passwordConfirmation(self,password, passwordconfirmation):
        if password == passwordconfirmation:
            self.report.label_26.setText("")
            return True
        else:
            self.report.label_26.setText("Senhas não correspondem")
            return False

    # function to validate some fields
    def nameValidator(self,name, label):
        print("validador2")
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
        print("validator1")
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
        # if it`s only edition there`s no need to check email again
        if self.comparative == 1:
            print("entrou")
            email = self.report.lineEdit_8.text()
        password = self.report.lineEdit_9.text()
        password_confirmation = self.report.lineEdit_10.text()

        # validators
        print("validator11")
        name_validator = self.nameValidator(name, self.report.label_3)
        print("validator12")
        surname_validator = self.nameValidator(surname, self.report.label_17)
        cpf_validator = self.cpf_validate(cpf)
        birth_date_validator = self.birthValidation(birth_date)
        city_validator = self.nameValidator(city, self.report.label_20)
        profession_validator = self.nameValidator(profession, self.report.label_21)
        team_validator = self.nameValidator(team, self.report.label_22)
        film_category_validator = self.nameValidator(film_category, self.report.label_23)
        password_validator = self.passwordValidation(password)
        password_confirmation_validator = self.passwordConfirmation(password, password_confirmation)
        # if it`s only edition there`s no need to check email again
        if self.comparative == 1:
            print("entrou2")
            email_validator = self.emailValidator(email, self.report.label_24)
        else:
            email_validator = True

        print("entrou3")
        validation = [name_validator, surname_validator, cpf_validator, birth_date_validator, city_validator,
                      profession_validator, team_validator, film_category_validator, email_validator,
                      password_validator,
                      password_confirmation_validator]

        #in new sign up needs to check email
        if self.comparative == 1:
            if False in validation:
                print("nok")
            else:
                password_validator, code = self.emailConfirmation(name, email)
                print(name, email)
                print(code)
                self.verification.show()
                self.verification.lineEdit.setText("")
                self.verification.pushButton_2.clicked.connect(lambda: self.compare_Code(code))

        elif False in validation:
            print("nok")
        else:
            print("tratar banco de dados")
            self.window_swap(self.wopen,self.wclose)