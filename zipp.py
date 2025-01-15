import zipfile
from tkinter import messagebox
import os

def zipp(name,file):
    try:
        with zipfile.ZipFile(os.path.join('./minhas_cifras', f'{name}.zip'), 'a', zipfile.ZIP_DEFLATED) as myzip:
            myzip.write(file)
            myzip.close()
    except Exception as erro:
        messagebox.showerror(message=f'Ouve um error cheque as informações\n{erro}')

if __name__ == '__main__':
    zipp('testando_zip', os.path.join('./minhas_cifras', f'testando.txt'))
