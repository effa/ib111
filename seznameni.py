# encoding: utf-8

# import funkci, ktere budeme potrebovat, z knihoven turtle, random a math
from turtle import *
from random import choice
from math import sin, cos, pi

# definice konstant
POCET_MIST = 28
POLOMER = 300


# nacte jmeno ze standardniho vstupu
def nacti_jmeno(vyzva):
    print vyzva,
    jmeno = raw_input()
    return jmeno


# nakresli caru ze soucasne pozice do daneho mista na kruznici
def nakresli_caru_do(misto):
    x = POLOMER * cos(2 * pi * misto / POCET_MIST)
    y = POLOMER * sin(2 * pi * misto / POCET_MIST)
    pendown()  # zapnuti kresleni
    goto(x, y)
    penup()  # vypnuti kresleni


# napise jmeno osoby na aktualni misto
def napis_jmeno(misto, jmeno):
    souradnice = position()
    # ruzne zarovnani podle pozice na kruznici
    if misto < 0.2 * POCET_MIST or misto > 0.8 * POCET_MIST:
        # prava cast
        zarovnani = 'left'
        setposition(souradnice + (11, -10))
    elif misto < 0.3 * POCET_MIST:
        # horni cast
        zarovnani = 'center'
        setposition(souradnice + (0, 5))
    elif misto < 0.7 * POCET_MIST:
        # leva cast
        zarovnani = "right"
        setposition(souradnice + (-8, -9))
    else:
        # dolni cast
        zarovnani = "center"
        setposition(souradnice + (0, -24))
    write(jmeno, align=zarovnani, font=('Arial', 12, 'normal'))
    setposition(souradnice)


# nacita zadana jmena a prubezne sit vykresluje
def vytvor_sit():
    # pripraveni zelvy
    hideturtle()
    penup()  # ted nekresli
    forward(POLOMER)
    # nacteme jmeno prvni osoby
    jmeno = nacti_jmeno('Prvni osoba:')
    # mapovani osob na jejich mista
    osoby = {jmeno: 0}
    # seznam volnych mist
    volna_mista = [p for p in range(1, POCET_MIST)]
    # skoncime, kdyz jsou vycerpany pozice nebo kdyz uzivatel napsal 'konec'
    while volna_mista and jmeno != 'konec':
        # pokud jeste nema osoba svoje misto, nahodne ji ho zvolime
        if jmeno not in osoby:
            misto = choice(volna_mista)
            osoby[jmeno] = misto
            volna_mista.remove(misto)
        else:
            misto = osoby[jmeno]
        # nakreslime vrchol, hranu a jmeno
        nakresli_caru_do(misto)
        napis_jmeno(misto, jmeno)
        dot(9)
        # nacteme dalsi jmeno
        jmeno = nacti_jmeno('Kdo pomuze:')
    # ukonceni kresleni
    done()

# po spusteni
vytvor_sit()
