# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
from time import sleep
import escala
import threading

nova_cifra = []
class Trans_Fm:
    def __init__(self, n_cifra, original, mudado, text_area, id=None):

        def t_Fm(self):
            if str(n_cifra) != '':
                try:
                    cifra = ''

                    
                    if original == 'Fm' and mudado == 'Am':
                        original_cifra = escala.A
                        sub = escala.Ast
                    
                    if original == 'Fm' and mudado == 'A#m':
                        original_cifra = escala.A
                        sub = escala.B

                    if original == 'Fm' and mudado == 'Bm':
                        original_cifra = escala.A
                        sub = escala.C
                   
                    if original == 'Fm' and mudado == 'Cm':
                        original_cifra = escala.A
                        sub = escala.Cst

                    if original == 'Fm' and mudado == 'C#m':
                        original_cifra = escala.A
                        sub = escala.D
                        
                    if original == 'Fm' and mudado == 'Dm':
                        original_cifra = escala.A
                        sub = escala.Dst
                        
                    if original == 'Fm' and mudado == 'D#m':
                        original_cifra = escala.A
                        sub = escala.E
                                  
                    if original == 'Fm' and mudado == 'Em':
                        original_cifra = escala.A
                        sub = escala.F

                    if original == 'Fm' and mudado == 'F#m':
                        original_cifra = escala.A
                        sub = escala.Fst

                    if original == 'Fm' and mudado == 'Gm':
                        original_cifra = escala.A
                        sub = escala.G

                    if original == 'Fm' and mudado == 'G#m':
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

                                    if original == 'Fm' and mudado == 'Am':
                                        

                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('Fm', 'Am')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('G#', '1do')
                                                    contar += 1
                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('A#m', '2rem')
                                                    contar += 1
                                                                                        
                                                if contar == 12:
                                                    cifra = cifra.replace('C', 'E')
                                                    contar += 1
                                                                                                                               
                                                if contar == 11:
                                                    cifra = cifra.replace('C#', 'F')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('D#', 'G')
                                                    contar += 1
                                                    
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/E')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('/E', '/5sol#')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/6la')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/G', '/7si')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('G', '7si')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('A#°', 'D°')
                                                    cifra = cifra.replace('Bb°', 'D°')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'A#m':
                                        

                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('Fm', '6la#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#', '1do#')
                                                    contar += 1
                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('A#m', 'D#m')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('C', '4fa')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', '4fa#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('D#', 'G#')
                                                    contar += 1
                                                    
                                                if contar == 1:
                                                    cifra = cifra.replace('/C', '/4fa')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/6la')
                                                    contar += 1
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('/F', '/6la#')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/1do')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('G', '1do')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('A#°', 'D#°')
                                                    cifra = cifra.replace('Bb°', 'D#°')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'Bm':
                                        

                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Fm', '7sim')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#', '2re')
                                                    contar += 1
                                                                                       
                                                if contar == 11:
                                                    cifra = cifra.replace('A#m', 'Em')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('C', 'F#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('C#', '5sol')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 9:
                                                    cifra = cifra.replace('D#', 'A')
                                                    contar += 1
                                                    
                                                if contar == 5:
                                                    cifra = cifra.replace('/C', '/4fa#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/A#')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/B')
                                                    contar += 1

                                                if contar == 10:
                                                    cifra = cifra.replace('/G', '/C#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('G', '1do#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', 'E°')
                                                    cifra = cifra.replace('Bb°', 'E°')
                                                    contar += 1
             
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'Cm':
                                        

                                            while TRUE:
                                                if contar == 10:
                                                    cifra = cifra.replace('Fm', 'Cm')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('G#', '2re#')
                                                    contar += 1
                                                                                       
                                                if contar == 7:
                                                    cifra = cifra.replace('A#m', '4fam')
                                                    contar += 1
                                                                                        
                                                if contar == 3:
                                                    cifra = cifra.replace('C', '5sol')
                                                    contar += 1
                                                                                                                               
                                                if contar == 5:
                                                    cifra = cifra.replace('C#', 'G#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('D#', 'A#')
                                                    contar += 1
                                                    
                                                if contar == 2:
                                                    cifra = cifra.replace('/C', '/5sol')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('/E', '/B')
                                                    contar += 1
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('/F', '/1do')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('/G', '/D')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('G', 'D')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', 'F°')
                                                    cifra = cifra.replace('Bb°', 'F°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'C#m':
                                        

                                            while TRUE:
                                                if contar == 6:
                                                    cifra = cifra.replace('Fm', '1do#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#', 'E')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('A#m', '4fa#m')
                                                    contar += 1
                                                                                        
                                                if contar == 9:
                                                    cifra = cifra.replace('C', 'G#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 3:
                                                    cifra = cifra.replace('C#', '6la')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 11:
                                                    cifra = cifra.replace('D#', 'B')
                                                    contar += 1
                                                    
                                                if contar == 7:
                                                    cifra = cifra.replace('/C', '/G#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/E', '/1do')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/1do#')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('/G', '/2re#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('G', '2re#')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', 'F#°')
                                                    cifra = cifra.replace('Bb°', 'F#°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'Dm':
                                        

                                            while TRUE:
                                                if contar == 11:
                                                    cifra = cifra.replace('Fm', 'Dm')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G#', '4fa')
                                                    contar += 1
                                                                                       
                                                if contar == 10:
                                                    cifra = cifra.replace('A#m', 'Gm')
                                                    contar += 1
                                                                                        
                                                if contar == 8:
                                                    cifra = cifra.replace('C', 'A')
                                                    contar += 1
                                                                                                                               
                                                if contar == 2:
                                                    cifra = cifra.replace('C#', '6la#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 9:
                                                    cifra = cifra.replace('D#', 'C')
                                                    contar += 1
                                                    
                                                if contar == 1:
                                                    cifra = cifra.replace('/C', '/6la')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/1do#')
                                                    contar += 1
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('/F', '/2re')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('/G', '/3mi')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('G', '3mi')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', 'G°')
                                                    cifra = cifra.replace('Bb°', 'G°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'D#m':
                                        

                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Fm', '2re#m')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#', '4fa#')
                                                    contar += 1
                                                                                       
                                                if contar == 11:
                                                    cifra = cifra.replace('A#m', 'G#m')
                                                    contar += 1
                                                                                        
                                                if contar == 10:
                                                    cifra = cifra.replace('C', 'A#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 4:
                                                    cifra = cifra.replace('C#', '7si')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 9:
                                                    cifra = cifra.replace('D#', '1do#')
                                                    contar += 1
                                                    
                                                if contar == 5:
                                                    cifra = cifra.replace('/C', '/A#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('/E', '/2re')
                                                    contar += 1
                                                
                                                if contar == 8:
                                                    cifra = cifra.replace('/F', '/2re#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/G', '/4fa')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G', '4fa')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', 'G#°')
                                                    cifra = cifra.replace('Bb°', 'G#°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'Em':
                                        

                                            while TRUE:
                                                if contar == 3:
                                                    cifra = cifra.replace('Fm', '3mim')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('G#', '5sol')
                                                    contar += 1
                                                                                       
                                                if contar == 1:
                                                    cifra = cifra.replace('A#m', '6lam')
                                                    contar += 1
                                                                                        
                                                if contar == 12:
                                                    cifra = cifra.replace('C', 'B')
                                                    contar += 1
                                                                                                                               
                                                if contar == 10:
                                                    cifra = cifra.replace('C#', '1do')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('D#', 'D')
                                                    contar += 1
                                                    
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/7si')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/E', '/2re')
                                                    contar += 1
                                                
                                                if contar == 5:
                                                    cifra = cifra.replace('/F', '/3mi')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('/G', '/4fa#')
                                                    contar += 1

                                                if contar == 4:
                                                    cifra = cifra.replace('G', '4fa#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('A#°', '6la°')
                                                    cifra = cifra.replace('Bb°', '6la°')
                                                    contar += 1
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'F#m':
                                        

                                            while TRUE:
                                                if contar == 4:
                                                    cifra = cifra.replace('Fm', '4fa#m')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('G#', '6la')
                                                    contar += 1
                                                                                       
                                                if contar == 2:
                                                    cifra = cifra.replace('A#m', '7sim')
                                                    contar += 1
                                                                                        
                                                if contar == 10:
                                                    cifra = cifra.replace('C', '1do#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 1:
                                                    cifra = cifra.replace('C#', '2re')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 8:
                                                    cifra = cifra.replace('D#', '3mi')
                                                    contar += 1
                                                    
                                                if contar == 9:
                                                    cifra = cifra.replace('/C', '/C#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/E', '/4fa')
                                                    contar += 1
                                                
                                                if contar == 12:
                                                    cifra = cifra.replace('/F', '/F#')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('/G', '/G#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('G', 'G#')
                                                    contar += 1

                                                if contar == 6:
                                                    cifra = cifra.replace('A#°', '7si°')
                                                    cifra = cifra.replace('Bb°', '7si°')
                                                    contar += 1
                                                    
                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'Gm':
                                        

                                            while TRUE:
                                                if contar == 7:
                                                    cifra = cifra.replace('Fm', '5solm')
                                                    contar += 1

                                                if contar == 1:
                                                    cifra = cifra.replace('G#', '6la#')
                                                    contar += 1
                                                                                       
                                                if contar == 4:
                                                    cifra = cifra.replace('A#m', '1dom')
                                                    contar += 1
                                                                                        
                                                if contar == 6:
                                                    cifra = cifra.replace('C', '2re')
                                                    contar += 1
                                                                                                                               
                                                if contar == 10:
                                                    cifra = cifra.replace('C#', '2re#')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 5:
                                                    cifra = cifra.replace('D#', '4fa')
                                                    contar += 1
                                                    
                                                if contar == 11:
                                                    cifra = cifra.replace('/C', '/2re')
                                                    contar += 1

                                                if contar == 3:
                                                    cifra = cifra.replace('/E', '/4fa#')
                                                    contar += 1
                                                
                                                if contar == 2:
                                                    cifra = cifra.replace('/F', '/4sol')
                                                    contar += 1

                                                if contar == 8:
                                                    cifra = cifra.replace('/G', '/6la')
                                                    contar += 1

                                                if contar == 9:
                                                    cifra = cifra.replace('G', '6la')
                                                    contar += 1

                                                if contar == 12:
                                                    cifra = cifra.replace('A#°', '1do°')
                                                    cifra = cifra.replace('Bb°', '1do°')
                                                    contar += 1

                                                    break
                                                break

                                    elif original == 'Fm' and mudado == 'G#m':
                                        

                                            while TRUE:
                                                if contar == 1:
                                                    cifra = cifra.replace('Fm', '5sol#m')
                                                    contar += 1

                                                if contar == 7:
                                                    cifra = cifra.replace('G#', '7si')
                                                    contar += 1
                                                                                       
                                                if contar == 12:
                                                    cifra = cifra.replace('A#m', '1do#m')
                                                    contar += 1
                                                                                        
                                                if contar == 13:
                                                    cifra = cifra.replace('C', '2re#')
                                                    contar += 1
                                                                                                                               
                                                if contar == 6:
                                                    cifra = cifra.replace('C#', '3mi')
                                                    contar += 1
                                                                                                                                                                       
                                                if contar == 9:
                                                    cifra = cifra.replace('D#', '4fa#')
                                                    contar += 1
                                                    
                                                if contar == 8:
                                                    cifra = cifra.replace('/C', '/2re#')
                                                    contar += 1

                                                if contar == 2:
                                                    cifra = cifra.replace('/E', '/5sol')
                                                    contar += 1
                                                
                                                if contar == 4:
                                                    cifra = cifra.replace('/F', '/5sol#')
                                                    contar += 1

                                                if contar == 5:
                                                    cifra = cifra.replace('/G', '/6la#')
                                                    contar += 1

                                                if contar ==10:
                                                    cifra = cifra.replace('G', '6la#')
                                                    contar += 1

                                                if contar == 11:
                                                    cifra = cifra.replace('A#°', '1do#°')
                                                    cifra = cifra.replace('Bb°', '1do#°')
                                                    contar += 1

                                                if contar == 3:
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
                                cifra = cifra.replace('fast', 'F#')
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
                                cifra = cifra.replace('12mm', 'C')
                                cifra = cifra.replace('m2', 'F')
                                cifra = cifra.replace('11m', 'Cm')
                                cifra = cifra.replace('dost', 'C#')
                                cifra = cifra.replace('dosust', 'C#')
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
        
        threading.Thread(target=t_Fm(self)).start()
