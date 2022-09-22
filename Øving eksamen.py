import math

def pi(d=2):
    print(round(math.pi, d))




def bank():
    saldo = 500
    rentesats = 0.01
    log = []
    print("""--------------------
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - siste endringer
--------------------""")
    if True:
        while True:
            a = int(input('Velg handling: '))
            if a is 1:
                print(saldo)

            elif a is 2:
                b = int(input('Hvor mye vil du sette inn? '))
                saldo += b
                log[:0] += ['+'+str(b)]
                if saldo > 1000000:
                    rentesats = 0.02
                    if 1000000 - b < 1000000:
                        print('Du får bonusrente!')

            elif a is 3:
                b = int(input('Hvor mye vil du ta ut? '))
                if b > saldo:
                    print('Beløpet overstiger saldoen din.')
                    continue
                saldo -= b
                log[:0] += [str(-b)]
                if saldo < 1000000:
                    rentesats = 0.01
                    if saldo + b > 1000000:
                        print('Du mistet bonusrenten din')
                

            elif a is 4:
                log[:0] += ['+'+str(rentesats*saldo)]
                saldo += rentesats*saldo
                print(saldo)

            elif a is 5:
                for element in log[0:3]:
                    print(element)

            else:
                a = input('Ugyldig verdi.    "Quit" for å avlsutte, any key for å fortsette:  ')
                if a.lower() == 'quit':
                    print('Avslutter')
                    quit

        




bank()
