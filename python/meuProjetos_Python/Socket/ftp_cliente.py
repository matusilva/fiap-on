from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

user = input("digite o user: ")
password = input("senha: ")

ftp.login(user, password)

print("DIR atual: ", ftp.pwd())
ftp.cwd('pub')

print("DIR corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()
