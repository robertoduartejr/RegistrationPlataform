import smtplib
import random

numbers = '0123456789'
code =''
name = 'Roberto'
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
    #type(smtpObj)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('pessoatestecsv@outloo.com','Senhacurso12345')
    smtpObj.sendmail('pessoatestecsv@outlook.com', 'robertoduartejrr@gmail.com', body) # Or recipient@outlook
except Exception as e:
    print("erro")

smtpObj.quit()