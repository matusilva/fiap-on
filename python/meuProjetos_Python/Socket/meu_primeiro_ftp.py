from ftplib import *
ftp = FTP('ftp.arquivo.org')
print(ftp.getwelcome())
ftp.quit()