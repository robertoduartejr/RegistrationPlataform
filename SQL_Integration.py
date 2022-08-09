import pyodbc


class SQL_Integration:

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

    def data_connection(self):
        data_connection = (
            "Driver={SQL Server};"
            "Server=LAPTOP-5PVO53D2;"
            "Database=Register_Plataform;"
        )
        connection = pyodbc.connect(data_connection)
        return connection