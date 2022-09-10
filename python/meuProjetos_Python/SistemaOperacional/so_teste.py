import platform
import getpass
from datetime import datetime


print("Nome maquina:........", platform.node())
print("Arquitetura:.........", platform.architecture())
print("Sistema Operacional:.", platform.system())
print("Versão do SO:........", platform.release())
print("Processador:.........", platform.processor())
print("Versão do python:....", platform.python_version())

print(datetime.now().month)

print(getpass.getuser())