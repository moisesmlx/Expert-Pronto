from escala import *


def ver_escalas(tom):
    if tom == 'A':
        nota = str(A1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Am':
        nota = str(Am).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'A#':
        nota = str(Ast1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'A#m':
        nota = str(Astm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'B':
        nota = str(B1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Bm':
        nota = str(Bm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'C':
        nota = str(C1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Cm':
        nota = str(Cm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'C#':
        nota = str(Cst1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'C#m':
        nota = str(Cstm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'D':
        nota = str(D1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Dm':
        nota = str(Dm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'D#':
        nota = str(Dst1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'D#m':
        nota = str(Dstm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'E':
        nota = str(E1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Em':
        nota = str(Em).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'F':
        nota = str(F1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Fm':
        nota = str(Fm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'F#':
        nota = str(Fst1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'F#m':
        nota = str(Fstm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'G':
        nota = str(G1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'Gm':
        nota = str(Gm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'G#':
        nota = str(Gst1).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    if tom == 'G#m':
        nota = str(Gstm).replace('[', '')
        nota = nota.replace(']', '')
        nota = nota.replace("'", '')
        return nota
    else:
        return 'Erro, Digite o tom em formato de cifra américana ex: "A, B, C, Am, Bm, Cm":'


if __name__ == '__main__':
    print(escala_detalhada('D#'))
