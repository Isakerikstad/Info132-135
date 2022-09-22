#Temaoppgave 4
#Temainnelvering 4 Isak Erikstad

#Oppgave 1


def siste(sekvens):
    print(sekvens[-1])

#Oppgave 2

def skriv_sekvens(sekvens):
    print(*sekvens)


#Oppgave 3


a = int(input('Startbeløp: '))
b = float(input('Rentesats (%):'))*0.01
c = int(input('Ønsket beløp: '))
år = 0

while a < c:
    år += 1
    a += b*a
    print('År', år, ' :', a, '\n')

"""
#Oppgave 4


print('  | 1  2  3  4  5  6  7  8  9')
print('--+-----------------------------')
print('1 | 1  2  3  4  5  6  7  8  9')
print('2 | 2  4  6  8 10 12 14 16 18')
print('3 | 3  6  9 12 15 18 21 24 27')
print('4 | 4  8 12 16 20 24 28 32 36')
print('5 | 5 10 15 20 25 30 35 40 45')
print('6 | 6 12 18 24 30 36 42 48 54')
print('7 | 7 14 21 28 35 42 49 56 63')
print('8 | 8 16 24 32 40 48 56 64 72')
print('9 | 9 18 27 36 45 54 63 72 81')

"""

#Alternativt oppgave 4

x = 0

print('   | 1   2   3   4   5   6   7   8   9 \n-----------------------------------------')

while x != 9:
    
    x += 1

    print(x, ' | ', end='')

    for svar in list(range(x, x*10, x)):
        if len(str(svar)) == 2:
            print(svar, end="  ")
        else:
            print(svar, end='   ')
    print()

        
    

    
