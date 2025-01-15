# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
from time import sleep
import escala
import threading

nova_cifra = []
class Trans_Ast:
    def __init__(self,n_cifra, original, mudado, text_area, id=None):
        def t_Ast(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    #Lá
                    if original.upper() == 'A#' and mudado.upper() == 'A':
                        original_cifra = escala.Ast
                        sub = escala.A
                    
                    if original.upper() == 'A#' and mudado.upper() == 'B':
                        original_cifra = escala.Ast
                        sub = escala.B

                    if original.upper() == 'A#' and mudado.upper() == 'C':
                        original_cifra = escala.Ast
                        sub = escala.C
                   
                    if original.upper() == 'A#' and mudado.upper() == 'C#':
                        original_cifra = escala.Ast
                        sub = escala.Cst

                    if original.upper() == 'A#' and mudado.upper() == 'D':
                        original_cifra = escala.Ast
                        sub = escala.D
                        
                    if original.upper() == 'A#' and mudado.upper() == 'D#':
                        original_cifra = escala.Ast
                        sub = escala.Dst
                        
                    if original.upper() == 'A#' and mudado.upper() == 'E':
                        original_cifra = escala.Ast
                        sub = escala.E
                                  
                    if original.upper() == 'A#' and mudado.upper() == 'F':
                        original_cifra = escala.Ast
                        sub = escala.F

                    if original.upper() == 'A#' and mudado.upper() == 'F#':
                        original_cifra = escala.Ast
                        sub = escala.Fst

                    if original.upper() == 'A#' and mudado.upper() == 'G':
                        original_cifra = escala.Ast
                        sub = escala.G

                    if original.upper() == 'A#' and mudado.upper() == 'G#':
                        original_cifra = escala.Ast
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
                                    if original.upper() == 'A#' and mudado.upper() == 'A':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'A')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'Bm')
                                                    contar += 1
                                                
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('D#', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Gm', 'F#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'G#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/C#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/F#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/G#')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'B':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'B')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('Cm', 'C#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Dm', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('D#', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('F', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Gm', 'G#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'A#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/D#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/G#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/A#')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'C':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('A#', 'C')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'Dm')
                                                    contar += 1
                                                
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('Dm', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('D#', 'F')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'G')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Gm', 'Am')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'B°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/E')

                                                if contar == 10:
                                                    cifra = cifra.replace('/G', '/A')

                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/B')
             
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'C#':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('A#', 'C#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'D#m')
                                                    contar += 1
                                                
                                                
                                                if contar == 1:
                                                    cifra = cifra.replace('Dm', 'Fm')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('D#', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'G#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Gm', 'A#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'C°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/F')

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/A#')

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/C')
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'D':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('A#', 'D')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Cm', 'Em')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Dm', 'F#m')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('D#', 'G')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('F', 'A')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Gm', 'Bm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'C#°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/F#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/B')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/C#')
                                                    contar += 1 
             
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'D#':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('A#', 'D#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('Cm', 'Fm')
                                                    contar += 1
                                                
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('Dm', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('D#', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('F', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Gm', 'Cm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('G#°', 'D°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/D', '/G')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/G', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/D')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'E':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 2:
                                                    cifra = cifra.replace('A#', 'E')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Cm', 'F#m')
                                                    contar += 1                                       
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('D#', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'B')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Gm', 'C#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'D#°')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/D', '/G#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/G', '/C#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/D#')
                                                    contar += 1 
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'F':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('A#', 'F')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('Cm', 'Gm')
                                                    contar += 1                                        
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('Dm', 'Am')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('D#', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'C')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('Gm', 'Dm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'E°')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/D', '/A')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/D')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/A', '/E')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'F#':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 5:
                                                    cifra = cifra.replace('A#', 'F#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'G#m')
                                                    contar += 1                                        
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'A#m')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('D#', 'B')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'C#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Gm', 'D#m')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'F°')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/A#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/D#')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/F')
                                                    contar += 1
                                                
                                                if contar == 11:
                                                    cifra = cifra.replace('/F#', '/A#')
                                                    contar += 1
                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'G':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'G')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'Am')
                                                    contar += 1                                       
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('D#', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'D')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Gm', 'Em')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'F#°')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/B')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/E')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/F#')
                                                    contar += 1

                                                    break
                                                break

                                    elif original.upper() == 'A#' and mudado.upper() == 'G#':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('A#', 'G#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('Cm', 'A#m')
                                                    contar += 1                                       
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'Cm')
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace('D#', 'C#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'D#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('Gm', 'Fm')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('A°', 'G°')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/D', '/C')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/F')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/G')
                                                    contar += 1
                                                    break
                                                break

                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace(str(original_cifra[18]), str(sub[18]))
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace(str(original_cifra[13]), str(sub[13]))
                                                    contar += 1
                                                
                                                
                                                if contar == 3:
                                                    cifra = cifra.replace(str(original_cifra[20]), str(sub[20]))
                                                    contar += 1
                                                                                        
                                                if contar == 4:
                                                    cifra = cifra.replace(str(original_cifra[23]), str(sub[23]))
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace(str(original_cifra[7]), str(sub[7]))
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace(str(original_cifra[11]), str(sub[11]))
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace(str(original_cifra[14]), str(sub[14]))
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

                                    if original.upper() == 'A' and mudado.upper() == 'C':
                                        cifra = cifra.replace('#', '')
                                        
                                    if mudado.upper() == 'A#' and original.upper() == 'A':
                                        cifra = cifra.replace('/D#', '/D')
                                        cifra = cifra.replace('/A#', '/A')
                                    if mudado.upper() == 'B' and original.upper() == 'A':
                                        cifra = cifra.replace('/F#', '/D#')
                                        cifra = cifra.replace('/E#', '/D#')
                                    if mudado.upper() == 'C#' and original.upper() == 'A':
                                            cifra = cifra.replace('C#9/F#', 'C#9/F')
                                    if mudado.upper() == 'C' and original.upper() == 'A':
                                            cifra = cifra.replace('Fm', 'Dm')

                            sleep(0.01)
                            

                            try:
                                cifra = cifra.replace('##', '#')
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
                                cifra = cifra.replace('Eb', 'D#')
                                cifra = cifra.replace('Bb', 'A#')
                                cifra = cifra.replace('G/A', 'G/B')
                                cifra = cifra.replace('G#/A', 'G#/C')
                                cifra = cifra.replace('B/A', 'B/D#')
                                cifra = cifra.replace('C/A', 'C/E')
                                cifra = cifra.replace('C#/A', 'C#/F')
                                cifra = cifra.replace('D/A', 'D/F#')
                                cifra = cifra.replace('D#/A', 'D#/G')
                                cifra = cifra.replace('E/A', 'E/G#')
                                cifra = cifra.replace('F#/A', 'F#/A#')
                                cifra = cifra.replace('##', '#')
                                
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
        threading.Thread(target=t_Ast(self)).start()
