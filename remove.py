import os
from time import strftime

lista = []
for pasta, subpasta, arquivo in os.walk('temporarios'):
    lista.append(arquivo)

for item in lista:
    for i in item:
        #os.system(fr'del /s /q temporarios\{i}')
        print(i)

os.system(r'del /s /q temporarios\Moi1178.txt')
