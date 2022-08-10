import pyodbc
from PyQt5 import uic,QtWidgets,QtGui, QtCore

class SQL_Integration:

    def getPassword(self, connection, email):
        cursor = connection.cursor()
        comando = f""" SELECT password FROM Usuarios
                    WHERE email = '{email}'"""
        cursor.execute(comando)
        row = cursor.fetchone()
        return row

    def allUserInformation(self,connection,email,report):
        print("chegoou aqui??")
        cursor = connection.cursor()
        comando = f""" SELECT * FROM Usuarios
                            WHERE email = '{email}'"""
        cursor.execute(comando)
        row = cursor.fetchone()
        print(row)

        print(row[3])
        qdate = QtCore.QDate.fromString(row[3], "yyyy-MMM-d")

        report.lineEdit.clear()
        report.lineEdit.insert(row[0])
        report.lineEdit_2.clear()
        report.lineEdit_2.insert(row[1])
        report.lineEdit_3.clear()
        report.lineEdit_3.insert(row[2])
        report.dateEdit.setDate(qdate)
        report.lineEdit_4.clear()
        report.lineEdit_4.insert(row[4])
        report.comboBox.setCurrentText(row[5])
        report.lineEdit_5.clear()
        report.lineEdit_5.insert(row[6])
        report.lineEdit_6.clear()
        report.lineEdit_6.insert(row[7])
        report.lineEdit_7.clear()
        report.lineEdit_7.insert(row[8])
        report.textEdit.clear()
        report.textEdit.setPlainText(row[9])
        report.textEdit_2.clear()
        report.textEdit_2.setPlainText(row[10])
        report.lineEdit_9.clear()
        report.lineEdit_9.insert(row[12])
        report.lineEdit_10.clear()
        report.lineEdit_10.insert(row[12])


    def writedown_signup(self, connection,name, surname,CPF,birth_date,city, uf, profession, soccer_team, film_category, to_do_list, buy_list, email, password):

        cursor = connection.cursor()

        comando = f""" INSERT INTO Usuarios (name, surname,CPF,birth_date,city, UF, profession, soccer_team, film_category, to_do_list, buy_list, email, password)
        VALUES ('{name}','{surname}','{CPF}','{birth_date}','{city}','{uf}','{profession}','{soccer_team}','{film_category}','{to_do_list}', '{buy_list}','{email}','{password}')"""

        cursor.execute(comando)
        cursor.commit()

    def writedown_edit(self, connection,name, surname,CPF,birth_date,city, uf, profession, soccer_team, film_category, to_do_list, buy_list, password):

        cursor = connection.cursor()

        comando = f""" INSERT INTO Usuarios (name, surname,CPF,birth_date,city, UF, profession, soccer_team, film_category, to_do_list, buy_list, password)
        VALUES ('{name}','{surname}','{CPF}','{birth_date}','{city}','{uf}','{profession}','{soccer_team}','{film_category}','{to_do_list}', '{buy_list}','{password}')"""

        cursor.execute(comando)
        cursor.commit()

    def readfrom(self,connection):
        cursor = connection.cursor()
        comando = f""" SELECT * FROM Usuarios"""

        cursor.execute(comando)
        rows = cursor.fetchall()
        return rows

    def updateinfo(self, connection,name, surname,CPF,birth_date,city, uf, profession, soccer_team, film_category, to_do_list, buy_list, email, password):
        cursor = connection.cursor()
        comando = f"""UPDATE Usuarios
SET name='{name}', surname = '{surname}',CPF = '{CPF}',birth_date = '{birth_date}',city = '{city}', UF = '{uf}', profession = '{profession}', soccer_team = '{soccer_team}', film_category = '{film_category}', to_do_list = '{to_do_list}', buy_list = '{buy_list}', password = '{password}'
WHERE email = '{email}' """
        cursor.execute(comando)
        cursor.commit()


    def data_connection(self):
        data_connection = (
            "Driver={SQL Server};"
            "Server=LAPTOP-5PVO53D2;"
            "Database=Register_Plataform;"
        )
        connection = pyodbc.connect(data_connection)
        return connection

