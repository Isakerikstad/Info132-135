#Hovedinnlevering Isak Erikstad


#Oppgave 1



import math

def pi(d=2):
    if 0<d<16:
        print(round(math.pi, d))
    elif d==0:
        print('%1.f' % math.pi)
    elif d>=16:
        print('Python printer kun 15 desimaler for pi. Derfor blir det:', math.pi)
    else:
        print('%.2f' % math.pi)

#Oppgave 2

#print ('Oppgave 2 \nSkriv temperaturKonvertering("temp. du ønsker konvertere"), og "C" eller "F" etter hva slags type det er')

def temperaturKonvertering(tall, CF=None):
    if CF=='C':
        return(tall, 'Celsius =', ((tall*9/5) + 32), 'Fahrenheit.')
    elif CF=='F':
        return(tall, 'Fahrenheit =', ((tall - 32) * 5/9), 'Celsius')
    else:
        return(tall, 'Celsius =', ((tall*9/5) + 32), 'Fahrenheit.')
    
#Oppgave 3 a)

saldo=500

#rentesatsen

rentesats=0.01

#if saldo>1000000:
#    rentesats=0.02
#else:
#    rentesats=0.01
    
def innskudd(innskudd):
    global saldo
    global rentesats
    saldo += innskudd
    if saldo-innskudd<1000000 and saldo>1000000:
        print('Gratulerer, du får bonusrente.')
        rentesats=0.02

def uttak(uttak):
    global saldo
    global rentesats
    saldo=saldo-uttak
    if uttak>saldo:
        saldo=saldo+uttak
        print('Overtrekk.')
    elif saldo+uttak>1000000 and saldo<=1000000:
        print ('Du har nå ordinær rente')
        rentesats=0.01
    

def beregn_rente():
    print(saldo*rentesats)

def renteoppgjør():
    global saldo
    global rentesats
    saldo += saldo*rentesats

#Oppgave 3 b)

#3c)

logliste = []

    
def velg():
    global logliste
    print('--------------------')
    print('1 - vis saldo')
    print('2 - innskudd')
    print('3 - uttak')
    print('4 - renteoppgjør')
    print('5 - siste handlinger')
    print('--------------------')
    d = int(input('Velg handling: '))
    if d == 1:
        print(saldo)
    elif d == 2:
        a = int(input('Beløp: '))
        innskudd(a)
        logliste += ['+'+str(a)]
    elif d == 3:
        b = int(input('Beløp: '))
        uttak(b)
        print('Saldo: ', saldo)
        logliste  += ['-'+str(b)]
    elif d == 4:
        renteoppgjør()
        logliste += ['+'+str(saldo*rentesats)]

#3c)
    elif d == 5:
        #for d in logliste:
            #if len(logliste)<=3:
            #print(d[-4:-1])
           # else:
        print(logliste[-4:-1])
            
    else:
        print('Velg handling 1, 2, 3, 4 eller 5')


#Oppgave 4

import random

def tre_tilfeldige():
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    tilfeldige = [a, b, c]
    tilfeldige.sort()
    print (tilfeldige)
    


