# coding:utf-8
# Les cartes tenen un nº: A,2-10,J,Q,K (total 13)
# Les cartes tenen un pal: cors, piques, trebols, diamants (total de 4)

from random import randint

# Generem la tirada de jugador1
j1num=randint(1,13)
j1pal=randint(1,4)

numero=j1num
if (j1num==11):
    numero="J"
if (j1num==12):
    numero="Q"
if (j1num==13):
    numero="K
    
if (j1pal==1):
    pal="P"
if (j1pal==2):
    pal="T"
if (j1pal==3):
    pal="D"
if (j1pal==4):
    pal="C"


print "Jugador 1 te: " , numero, "de " , pal


# Generem la tirada de jugador2 (agafa una carta aleatoria)
j2num=randint(1,13)
j2pal=randint(1,4)

numero=j2num
if (j2num==11):
    numero="J"
if (j2num==12):
    numero="Q"
if (j2num==13):
    numero="K"

if (j2pal==1):
    pal="P"
if (j2pal==2):
    pal="T"
if (j2pal==3):
    pal="D"
if (j2pal==4):
    pal="C"

print "Jugador 2 te: " , numero, "de " , pal

# Comprovem si hi ha empat
if (j1num==j2num):
    print “Empat”
else:
    if (j1num>j2num):
        print “Guanya jugador1”
    else:
        print “Guanya jugador2”
