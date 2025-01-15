import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4


def create_pdf(name_txt, name_pdf):
    with open(f'{name_txt}.txt', 'r', encoding = 'utf-8') as arq:
        dic = arq.readlines()
        
    w, h = A4
    c = canvas.Canvas(f'{name_pdf}.pdf', pagesize=A4)

    # Move a origem do cursor para a parte superior esquerda
    c.translate(inch,inch)

    # Inicia um objeto texto limitando a área para que linhas 
    # muito grandes, não ultrapassem a margem.
    textobject = c.beginText(0, 650)
    textobject.setFont("Times-Roman", 14)

    # Percorrendo o dicionário definido anteriormente
    #c.drawImage("logo.png", 50, h - 200)
    for lines in dic:
        textobject.textLines(lines)

    c.drawText(textobject)

    c.showPage()
    c.save()
