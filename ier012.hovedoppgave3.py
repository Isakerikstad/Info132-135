import json
from random import *

spar_s = '\u2660'
ruter_s = '\u2666'
kløver_s = '\u2663'
hjerter_s = '\u2665'

def reset():
    global kortstokk, kortplassering, bunker, antall_kort
    kortstokk = []
    kortplassering = ['A','B','C','D','E','F','G','H']
    bunker = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[]}
    antall_kort = {'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,'G':4,'H':4}

def lag_kortstokk():
    for t in range(7,15):
        label = '' #Nå trernger jeg bare sammenligne andreindeksen av de ulike kortene
        if t == 11:
            label = 'J'
        elif t == 12:
            label = 'Q'
        elif t == 13:
            label = 'K'
        elif t == 14:
            label = 'A'
        else:
            label = t
        kortstokk.append(f'\u2660 {label}')
        kortstokk.append(f'\u2666 {label}')
        kortstokk.append(f'\u2663 {label}')
        kortstokk.append(f'\u2665 {label}')
    shuffle(kortstokk)

def del_ut_4(bunke):
    global bunker, kortstokk
    A = 0
    for element in kortstokk[:]:
        A += 1
        bunker[bunke].append(element)
        kortstokk.remove(element)
        if A == 4:
            return bunker and kortstokk
            break

def åtte_bunker():
    for a in kortplassering:
        del_ut_4(a)

def dele_ut():
    global bunker, kortstokk

    a = 0
    for values in bunker.values():
        print (kortplassering[a], values[0], antall_kort[kortplassering[a]])
        a += 1

def spilltrekk(første, andre):
    global bunker
    if bunker[første][0][2] == bunker[andre][0][2]:
        if antall_kort[første] == 1 and antall_kort[andre] == 1:
            bunker[første] = ['- -']
            bunker[andre] = ['- -']
            antall_kort[første] = 0
            antall_kort[andre] = 0

        elif antall_kort[første] == 1:
            bunker[første] = ['- -']
            bunker[andre].remove(bunker[andre][0])
            antall_kort[første] = 0
            antall_kort[andre] -= 1

        elif antall_kort[andre] == 1:
            bunker[første].remove(bunker[første][0])
            bunker[andre] = ['- -']
            antall_kort[andre] = 0
            antall_kort[første] -= 1

        else:
            bunker[første].remove(bunker[første][0])
            bunker[andre].remove(bunker[andre][0])
            antall_kort[første] -= 1
            antall_kort[andre] -= 1
    else:
        print('De er ikke like')

def sjekk_tap():
    global d, bunker
    øverste_kort = []
    liste = øverste_kort
    a = 0
    for values in bunker.values():
        øverste_kort += values[0][2]
    for element in øverste_kort:
        liste.remove(element)
        if element in liste and element != '-':
            a += 1

    if a == 0:
        d = 'meny'
    else:
        d = 0
    c = 0
    for verdier in antall_kort.values():
        c += verdier
    if c == 0:
        d = 'seier'


def spill():
    while True:

        a = input('Velg to bunker: \n')

        if a.isnumeric():
            print('Velg to av bunkene. A-H...\n')

        elif len(a) == 2 and a.isalpha():
            l = list(a)
            første = l[0]
            andre = l[1]
            if første.upper() not in kortplassering:
                dele_ut()
                print('\nUgyldig trekk... Velg fra A til H')
            elif andre.upper() not in kortplassering:
                dele_ut()
                print('\nUgyldig trekk... Velg fra A til H')
            else:
                spilltrekk(første.upper(), andre.upper())
                dele_ut()
                sjekk_tap()
                if d == 'meny':
                    print('Ingen gyldige trekk...\nGame over!')
                    break
                elif d == 'seier':
                    print('DU VANT!!!!!!!!!!!')
                    replay = input('Vil du spill igjen?')
                    if replay == 'ja':
                        break
                    else:
                        quit()

        elif a == 'save':
            lagre()
            print('Spillet er lagret')

        elif a == 'quit':
            quit()

        elif a == 'menu':
            l = input('Vil du lagre først?')
            if l.upper() == 'JA' or l.upper() == 'YES' or l.upper() == 'OK':
                print('lagrer...')
                lagre()
            break

        else:
            print('Ugyldig verdi!\n')

def load():
    global bunker, antall_kort, d
    try:
        fil = open('kortspill.json','r')
        b = fil.read()
        bunker = json.loads(b)
        fil.close()
        d = 'funnet'
        for kort in bunker.keys():
            a = bunker[kort]
            antall_kort[kort] = len(a)
    except:
        print('Fant ikke noe spill')

def lagre():
    global bunker
    fil = open("kortspill.json", "w")
    json.dump(bunker, fil)
    fil.close()

def start():
    global d, kortstokk, bunker

    while True:

        d = input('"play","load" or "quit":\n ')
        if d.isnumeric():
            print('Du må skrive "play","load" or "quit"')

        elif d == 'play':
            print('spillet starter... \n'
                  'Tips: skriv "save" når som helst for å lagre spillet på datamskinen\n'
                  'Eller skriv "menu" for å gå tilbake til')
            reset()
            lag_kortstokk()
            åtte_bunker()
            dele_ut()
            sjekk_tap()

            while d == 'meny': #Passe på at man deler ut et bord man kan spille på
                print('Ingen mulige valg. Stokker ut på nytt')

                for values in bunker.values():
                    shuffle(values)
                dele_ut()
                sjekk_tap()

            spill()

        elif d == 'load':
            reset()
            load()
            if d == 'funnet':
                print('Oppretter lagret bord...')
                dele_ut()
                sjekk_tap()
                spill()


        elif d == 'quit':
            break

        else:
            print('Ugyldig verdi!\n')

start()

