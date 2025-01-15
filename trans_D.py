# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
from time import sleep
import escala
import threading

nova_cifra = []
class Trans_D:
    def __init__(self, n_cifra, original, mudado, text_area, id=None):

        def t_D(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    #B
                    if original.upper() == 'D' and mudado.upper() == 'A':
                        original_cifra = escala.B
                        sub = escala.A
                    
                    if original.upper() == 'D' and mudado.upper() == 'A#':
                        original_cifra = escala.B
                        sub = escala.Ast

                    if original.upper() == 'D' and mudado.upper() == 'B':
                        original_cifra = escala.B
                        sub = escala.C
                   
                    if original.upper() == 'D' and mudado.upper() == 'C':
                        original_cifra = escala.B
                        sub = escala.Cst

                    if original.upper() == 'D' and mudado.upper() == 'C#':
                        original_cifra = escala.B
                        sub = escala.D
                        
                    if original.upper() == 'D' and mudado.upper() == 'D#':
                        original_cifra = escala.B
                        sub = escala.Dst
                        
                    if original.upper() == 'D' and mudado.upper() == 'E':
                        original_cifra = escala.B
                        sub = escala.E
                                  
                    if original.upper() == 'D' and mudado.upper() == 'F':
                        original_cifra = escala.B
                        sub = escala.F

                    if original.upper() == 'D' and mudado.upper() == 'F#':
                        original_cifra = escala.B
                        sub = escala.Fst

                    if original.upper() == 'D' and mudado.upper() == 'G':
                        original_cifra = escala.B
                        sub = escala.G

                    if original.upper() == 'D' and mudado.upper() == 'G#':
                        original_cifra = escala.B
                        sub = escala.Gst


                    with open(f'temporarios/{id}.txt', 'w', encoding='utf-8') as texto:
                        texto.write(text_area)

                    with open(f'temporarios/{id}.txt', 'r', encoding='utf-8') as texto:
                        te = texto.readlines()
                        for i in range(len(te)):
                            contar = 1
                            confere = TRUE
                            if 'Solo]' in str(te[i]) or 'solo]' in str(te[i]) or 'SOLO]' in str(te[i])\
                                or 'Solo' in str(te[i]) or 'SOLO' in str(te[i]) or '|' in str(te[i]) or '-' in str(te[i])\
                                or 'Intro]' in str(te[i]) or 'intro]' in str(te[i]) or 'INTRO]' in str(te[i]) or 'INTRO' in str(te[i]) or 'Tom:' in str(te[i])\
                                or 'tom:' in str(te[i]) or 'TOM:' in str(te[i]) or ']' in str(te[i]) or 'primeira parte]' in str(te[i])\
                                or 'segunda parte]' in str(te[i]) or 'Primeira Parte]' in str(te[i]) or 'Segunda Parte]' in str(te[i]):
                                confere = TRUE
                            
                            else:
                                if '.' in str(te[i]) or ',' in str(te[i]) or 'l' in str(te[i]) or ':' in str(te[i]) or ';' in str(te[i]) or 'o' in str(te[i]) or 'u' in str(te[i]) or 'i' in str(te[i]) or '?' in str(te[i]) or 'p' in str(te[i]) or 'c' in str(te[i]) or 'a' in str(te[i])or 'e' in str(te[i] or 'f' in str(te[i])) or 'h' in str(te[i]) or 'n' in str(te[i]) or 'p' in str(te[i]) or 'r' in str(te[i]) or 'q' in str(te[i]) or 'z' in str(te[i]) or 'j' in str(te[i]):
                                    cifra = str(te[i])
                                    confere = FALSE

                            if confere:
                                cifra = str(te[i])
                                    
                                for x in range(len(original_cifra)):

                                    #exceções
                                    if original.upper() == 'D' and mudado.upper() == 'A':
                                        

                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('D', 'A')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('F#m', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('G', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('A', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Bm', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'G#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F#', '/C#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/F#')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/C#', '/G#')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'A#':
                                        

                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('D', 'A#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('Em', 'Cm')
                                                    contar += 1
                                                
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('F#m', 'Dm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('G', 'D#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('A', 'F')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Bm', 'Gm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'A°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/D')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/G')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/A')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'B':
                                        

                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('D', 'B')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Em', 'C#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('F#m', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('A', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Bm', 'G#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'A#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/D#')

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/G#')

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/A#')
             
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'C':
                                        

                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('D', 'C')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Em', 'Dm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('F#m', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'F')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('A', 'G')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Bm', 'Am')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'B°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/E')

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/A')

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/B')
                                                    
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'C#':
                                        

                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('D', 'C#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Em', 'D#m')
                                                    contar += 1
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('F#m', 'Fm')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('G', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('A', 'G#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Bm', 'A#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'C°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/F')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/A#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/C')
                                                    contar += 1 
             
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'D#':
                                        

                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('D', 'D#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Em', 'Fm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('F#m', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('A', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Bm', 'Cm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'D°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F#', '/G')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/C')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/C#', '/D')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'E':
                                        

                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('D', 'E')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('Em', 'F#m')
                                                    contar += 1                                       
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('F#m', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('A', 'B')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('Bm', 'C#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'D#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F#', '/G#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/C#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/D#')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'F':
                                        

                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('D', 'F')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Em', 'Gm')
                                                    contar += 1                                        
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('F#m', 'Am')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('A', 'C')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 7:
                                                    cifra = cifra.replace('Bm', 'Dm')
                                                    contar += 1
                                                    
                                                if contar == 1:
                                                    cifra = cifra.replace('C#°', 'E°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/A')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/B', '/D')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/E')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'F#':
                                        

                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('D', 'F#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Em', 'G#m')
                                                    contar += 1                                        
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('F#m', 'A#m')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'B')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('A', 'C#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Bm', 'D#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'F°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/F#', '/A#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/D#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/F')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'G':
                                        

                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('D', 'G')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Em', 'Am')
                                                    contar += 1                                       
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('F#m', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('A', 'D')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Bm', 'Em')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'F#°')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/F#', '/B')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/E')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/C#', '/F#')
                                                    contar += 1

                                                    break
                                                break

                                    elif original.upper() == 'D' and mudado.upper() == 'G#':
                                        

                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('D', 'G#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Em', 'A#m')
                                                    contar += 1                                       
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('F#m', 'Cm')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'C#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('A', 'D#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Bm', 'Fm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('C#°', 'G°')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/F#', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/F')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/C#', '/G')
                                                    contar += 1
                                                    break
                                                break
                                            
                                    else:
                                        contar = 1
                                        cifra = cifra.replace(str(original_cifra[x]), str(sub[x]))
                                        cifra = cifra.replace('##', '#')
                                        
                                    if mudado.upper() == 'B' and original.upper() == 'A':
                                        cifra = cifra.replace('/F#', '/D#')
                                        cifra = cifra.replace('B#', 'A#')

                            sleep(0.01)
                            

                            try:
                                cifra = cifra.replace('##', '#')
                                cifra = cifra.replace('A/A', 'A/C#')
                                cifra = cifra.replace('A9/A', 'A9/C#')
                                cifra = cifra.replace('A#/A#', 'A#/D')
                                cifra = cifra.replace('A#9/A#', 'A#9/D')
                                cifra = cifra.replace('B/B', 'B/D#')
                                cifra = cifra.replace('B9/B', 'B9/D#')
                                cifra = cifra.replace('C/C', 'C/E')
                                cifra = cifra.replace('C9/C', 'C9/E')
                                cifra = cifra.replace('C#/C#', 'C#/F')
                                cifra = cifra.replace('C#9/C', 'C#9/F')
                                cifra = cifra.replace('D/D', 'D/F#')
                                cifra = cifra.replace('D9/D', 'D9/F#')
                                cifra = cifra.replace('D#/D#', 'D#/G')
                                cifra = cifra.replace('D#9/D#', 'D#9/G')
                                cifra = cifra.replace('G/G', 'G/B')
                                cifra = cifra.replace('G#/G#', 'G#/C')
                                cifra = cifra.replace('G#/A#', 'G#/C')
                                cifra = cifra.replace('E/F#', 'E/G#')
                                cifra = cifra.replace('F/G#', 'F/A')
                                cifra = cifra.replace('C#/D#', 'C#/F')
                                cifra = cifra.replace('D/E#', 'D/F#')
                                cifra = cifra.replace('D#/F#', 'D#/G')
                                cifra = cifra.replace('F#/C', 'F#/A#')
                                cifra = cifra.replace('A#/D#', 'A#/D')
                                cifra = cifra.replace('F#/A##', 'F#/A#')
                                cifra = cifra.replace('G/C#', 'G/B')
                                
                            except: pass
                            with open(fr'Minhas_cifras/{n_cifra}.txt', 'a', encoding='utf-8') as arquivo:
                                if cifra == '\n':
                                    pass
                                else:
                                    if 'Solo]' in str(te[i]) or 'solo]' in str(te[i]) or 'SOLO]' in str(te[i])\
                                        or 'Solo' in str(te[i]) or 'SOLO' in str(te[i]) or '|' in str(te[i]) or '-' in str(te[i])\
                                        or 'Intro]' in str(te[i]) or 'intro]' in str(te[i]) or 'INTRO]' in str(te[i]) or 'INTRO' in str(te[i]) or 'Tom:' in str(te[i])\
                                        or 'tom:' in str(te[i]) or 'TOM:' in str(te[i]) or ']' in str(te[i]) or 'primeira parte]' in str(te[i])\
                                        or 'segunda parte]' in str(te[i]) or 'Primeira Parte]' in str(te[i]) or 'Segunda Parte]' in str(te[i]):
                                        arquivo.write('\n')
                                        nova_cifra.append('\n')
                                    arquivo.write(str(cifra))
                                    nova_cifra.append(str(cifra))

                except Exception as error:
                    erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}'
            else:
                erro=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!'
        
        threading.Thread(target=t_D(self)).start()
