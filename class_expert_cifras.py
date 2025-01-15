# _*_ coding:utf-8 _*_
from trans_A import *
from trans_Am import *
from trans_Astm import *
from trans_Ast import *
from trans_B import *
from trans_Bm import *
from trans_C import *
from trans_Cm import *
from trans_Cst import *
from trans_Cstm import *
from trans_D import *
from trans_Dm import *
from trans_Dst import *
from trans_Dstm import *
from trans_E import *
from trans_Em import *
from trans_F import *
from trans_Fm import *
from trans_Fst import *
from trans_Fstm import *
from trans_G import *
from trans_Gm import *
from trans_Gst import *
from trans_Gstm import *
from enviar_file import *
#from pdf import *
from escala import *

#Deploy em vercel iste gratuito
new = ''

class Cifras():
    def __init__(self, n_cifra, original, mudado, text_area, id=None):
        
        def translate(self):
                global new, confirm
                confirm = False
                if str(n_cifra) != '':
                    try:
                        if original.upper() == 'A':
                            Trans_A(n_cifra, original, mudado, text_area, id)
                        if original == 'Am':
                            Trans_Am(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'A#':
                            Trans_Ast(n_cifra, original, mudado, text_area, id)
                        if original == 'A#m':
                            Trans_Astm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'B':
                            Trans_B(n_cifra, original, mudado, text_area, id)
                        if original == 'Bm':
                            Trans_Bm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'C':
                            Trans_C(n_cifra, original, mudado, text_area, id)              
                        if original == 'Cm':
                            Trans_Cm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'C#':
                            Trans_Cst(n_cifra, original, mudado, text_area, id)
                        if original == 'C#m':
                            Trans_Cstm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'D':
                            Trans_D(n_cifra, original, mudado, text_area, id)
                        if original == 'Dm':
                            Trans_Dm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'D#':
                            Trans_Dst(n_cifra, original, mudado, text_area, id)
                        if original == 'D#m':
                            Trans_Dstm(n_cifra, original, mudado, text_area, id)
                            for l in nova_cifra:
                                new += f'{str(l)}'
                        if original.upper() == 'E':
                            Trans_E(n_cifra, original, mudado, text_area, id)
                        if original == 'Em':
                            Trans_Em(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'F':
                            Trans_F(n_cifra, original, mudado, text_area, id)
                        if original == 'Fm':
                            Trans_Fm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'F#':
                            Trans_Fst(n_cifra, original, mudado, text_area, id)
                        if original == 'F#m':
                            Trans_Fstm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'G':
                            Trans_G(n_cifra, original, mudado, text_area, id)
                        if original == 'Gm':
                            Trans_Gm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'G#':
                            Trans_Gst(n_cifra, original, mudado, text_area, id)
                        if original == 'G#m':
                            Trans_Gstm(n_cifra, original, mudado, text_area, id)

                        #from time import sleep
                        #sleep(2)

                        '''with open(fr'Minhas_cifras/{n_cifra}.txt', 'r', encoding='utf-8') as texto:
                            self.nova_cifra = str(texto.read())'''

                            #create_pdf(fr'static/Minhas_cifras/{n_cifra}', f'Minhas_cifras/{n_cifra}')
                        
                        #messagebox.showinfo(title='info', message=f'Sucesso, a troca de escala foi concluída de "{original}" para "{mudado}"')
                    except Exception as error:
                        pass
                        #messagebox.showerror(title='ERRO!', message=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}')

                else:
                    pass
                    #messagebox.showerror(title='ERRO!', message='Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!')

        translate(self)

if __name__ == '__main__':
    Cifras('Testando', 'A', 'C', 'A Bm C#m D E F#m G#°', 'nome_cifra')
    print(new)
