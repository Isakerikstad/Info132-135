#Temaoppgave 7 
#Oppgave 1

with open('telefon.txt', 'a') as tlf:
    a = input('Navn og nummer: ')
    while a != '':
        tlf.write('\n' + a)
        a = input('Navn og nummer: ')

tlf = open('telefon.txt')
print (tlf.read())
tlf.close()

#Oppgave 2
with open('telefon.txt', 'r') as tlf:
    with open('telefon.kopi.txt', 'w') as tlf_copy:
        n = input('\nNavn: ')
            
        for line in tlf:
            if n in line:
                print('Gammelt nummer er:' + line.strip(n))
                nummer = input('Nytt nummer er (enter for ingen nye endringer): ')
                if nummer == '':
                    break
                tlf_copy.write(f'{n} {nummer}\n')
                continue
            tlf_copy.write(line)

tlf = open('telefon.kopi.txt')
print (tlf.read())
tlf.close()

#Oppgave 3

def fjernVokaler(filnavn):
    innfil = open(filnavn)
    utfil = open('Uten-vokaler-'+filnavn,'w')
    for linje in innfil:
        for tegn in linje:
            if tegn in 'aeiouyæøåAEIOUYÆØÅ':
                tegn= ''
            utfil.write(tegn)
    innfil.close()
    utfil.close()

    
