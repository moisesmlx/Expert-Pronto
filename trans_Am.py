# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
import os
import pyautogui
from time import sleep
import clipboard
import escala
import threading


nova_cifra = []
class Trans_Am:
    def __init__(self, n_cifra, original, mudado, text_area, id):
        
        def t_Am(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    #Lá
                    if original == 'Am' and mudado == 'A#m':
                        original_cifra = escala.A
                        sub = escala.Ast
                    
                    if original == 'Am' and mudado == 'Bm':
                        original_cifra = escala.A
                        sub = escala.B

                    if original == 'Am' and mudado == 'Cm':
                        original_cifra = escala.A
                        sub = escala.C
                   
                    if original == 'Am' and mudado == 'C#m':
                        original_cifra = escala.A
                        sub = escala.Cst

                    if original == 'Am' and mudado == 'Dm':
                        original_cifra = escala.A
                        sub = escala.D
                        
                    if original == 'Am' and mudado == 'D#m':
                        original_cifra = escala.A
                        sub = escala.Dst
                        
                    if original == 'Am' and mudado == 'Em':
                        original_cifra = escala.A
                        sub = escala.E
                                  
                    if original == 'Am' and mudado == 'Fm':
                        original_cifra = escala.A
                        sub = escala.F

                    if original == 'Am' and mudado == 'F#m':
                        original_cifra = escala.A
                        sub = escala.Fst

                    if original == 'Am' and mudado == 'Gm':
                        original_cifra = escala.A
                        sub = escala.G

                    if original == 'Am' and mudado == 'G#m':
                        original_cifra = escala.A
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

                                    if original == 'Am' and mudado == 'A#m':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Am', 'A#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'C#')
                                                    contar += 1
                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('Dm', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('E', 'F')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('F', 'F#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('G', 'G#')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/F')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G#', '/A')
                                                    contar += 1
                                                
                                                if contar == 6:
                                                    cifra = cifra.replace('/A', '/A#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/B', '/C')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('B', 'C')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'D#°')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Bm':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'Bm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('C', '2re')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Dm', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 9:
                                                    cifra = cifra.replace('E', '4fa#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 8:
                                                    cifra = cifra.replace('F', '5sol')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('G', '6la')
                                                    contar += 1
                                                    
                                                if contar == 11:
                                                    cifra = cifra.replace('/E', '/4fa#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/G#', '/6la#')
                                                    contar += 1
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('/A', '/7si')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('/B', '/1do#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('B', '1do#')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('D°', '3mi°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Cm':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('Am', 'Cm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('C', '2re#')
                                                    contar += 1
                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('Dm', '4fam')
                                                    contar += 1
                                                                                        
                                                if contar == 7:
                                                    cifra = cifra.replace('E', 'G')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('F', '5sol#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'A#')
                                                    contar += 1
                                                    
                                                if contar == 4:
                                                    cifra = cifra.replace('/E', '/G')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/G#', '/7si')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/C')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/B', '/D')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('B', 'D')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'F°')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'C#m':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Am', 'C#m')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('C', 'E')
                                                    contar += 1
                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('Dm', 'F#m')
                                                    contar += 1
                                                                                        
                                                if contar == 5:
                                                    cifra = cifra.replace('E', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 7:
                                                    cifra = cifra.replace('F', 'A')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('G', '7si')
                                                    contar += 1
                                                    
                                                if contar == 4:
                                                    cifra = cifra.replace('/E', '/5sol#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('/G#', '/1do')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/1do#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('/B', '/D#')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('B', 'D#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'F#°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Dm':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Am', 'Dm')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('C', 'F')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Dm', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('E', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 6:
                                                    cifra = cifra.replace('F', 'A#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('G', 'C')
                                                    contar += 1
                                                    
                                                if contar == 4:
                                                    cifra = cifra.replace('/E', '/A')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/G#', '/C#')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/D')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('/B', '/E')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('B', 'E')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'G°')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'D#m':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Am', 'D#m')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('C', 'F#')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('Dm', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('E', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('F', 'SI')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('G', 'C#')
                                                    contar += 1
                                                    
                                                if contar == 4:
                                                    cifra = cifra.replace('/E', '/A#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/G#', '/D')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/D#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('/B', '/F')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('B', 'F')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'G#°')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Em':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('Am', 'Em')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('C', 'G')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'Am')
                                                    contar += 1
                                                                                        
                                                if contar == 2:
                                                    cifra = cifra.replace('E', 'B')
                                                    contar += 1
                                                                                                                               
                                                if contar == 7:
                                                    cifra = cifra.replace('F', 'C')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('G', 'D')
                                                    contar += 1
                                                    
                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/B')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G#', '/D#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/E')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/B', '/F#')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('B', '4#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'A°')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Fm':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('Am', 'Fm')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('C', 'G#')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'A#m')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('E', 'C')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'C#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('G', 'D#')
                                                    contar += 1
                                                    
                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/C')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G#', '/E')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/F')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/B', '/G')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('B', 'G')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'A#°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'F#m':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('Am', 'F#m')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('C', 'A')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'Bm')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('E', 'C#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'D')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('G', 'E')
                                                    contar += 1
                                                    
                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/C#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G#', '/F')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/F#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/B', '/G#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('B', '5#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'B°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'Gm':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('Am', 'Gm')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('C', 'A#')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('Dm', 'Cm')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('E', 'D')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('F', 'D#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 6:
                                                    cifra = cifra.replace('G', 'F')
                                                    contar += 1
                                                    
                                                if contar == 8:
                                                    cifra = cifra.replace('/E', '/D')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G#', '/F#')
                                                    contar += 1
                                                
                                                if contar == 10:
                                                    cifra = cifra.replace('/A', '/5sol')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/B', '/A')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('B', 'A')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('D°', 'C°')
                                                    contar += 1

                                                    break
                                                break

                                    elif original == 'Am' and mudado == 'G#m':
                                        
                                        
                                        if confere:
                                            
                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('Am', 'G#m')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('C', 'B')
                                                    contar += 1
                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('Dm', 'C#m')
                                                    contar += 1
                                                                                        
                                                if contar == 1:
                                                    cifra = cifra.replace('E', 'D#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('F', 'E')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 3:
                                                    cifra = cifra.replace('G', 'F#')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/D#')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/G#', '/G')
                                                    contar += 1
                                                
                                                if contar == 9:
                                                    cifra = cifra.replace('/A', '/G#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/B', '/A#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('B', 'A#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('D°', 'C#°')
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

                                    if mudado.upper() == 'C':
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
                                cifra = cifra.replace('SI', 'B')
                                cifra = cifra.replace('Bb', 'A#')
                                cifra = cifra.replace('Eb', 'D#')
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
                                cifra = cifra.replace('3°', 'E°')
                                cifra = cifra.replace('4#', 'F#')
                                cifra = cifra.replace('5#', 'G#')
                                cifra = cifra.replace('1do', 'C')
                                cifra = cifra.replace('2re', 'D')
                                cifra = cifra.replace('3mi', 'E')
                                cifra = cifra.replace('4fa', 'F')
                                cifra = cifra.replace('5sol', 'G')
                                cifra = cifra.replace('6la', 'A')
                                cifra = cifra.replace('7si', 'B')
                                
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
        threading.Thread(target= t_Am(self)).start()
