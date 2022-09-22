#INFO132 Obligatorisk hovedinnlevering 2. a og b i samme program.
#Isak Erikstad


def meny():
    print('--------------------')
    print('1 - Emneliste')
    print('2 - Legg til emne')
    print('3 - Sett karakter')
    print('4 - Karaktersnitt')
    print('5 - Avslutt')
    print('6 - Lagre')
    print('--------------------')

def godkjent_emne(emne): #Liten emnevalidator, kan forbedres
    if len(emne) == 7 and emne[-3].isnumeric() and int(emne[-3]) in range(1,4) and not emne[1].isnumeric():
        return emne.upper()

    elif len(emne) == 6 and emne[-3].isnumeric() and int(emne[-3]) in range(1,4) and not emne[1].isnumeric():
       return emne.upper()
    
    else:
        print('ugyldig emne/fagkode. Prøv skrive i dette formatet: GEO123 eller ECON321')
        return None

def godkjent_karakter(karakter):
    mulighetene = ['A', 'B', 'C', 'D', 'E', 'F']
    if karakter.upper() in mulighetene:
        return karakter.upper()
    elif karakter is '':
        return 'SLETT'
    elif karakter.isnumeric():
        print('Velg en bokstav-karakter')
        ny_karakter()
    else:
        print('Ugyldig karakter')

def ny_karakter():
    global karakterer, emneliste
    fag = godkjent_emne(input('emne: ')) #Kan legge til karakterer til fag som ennå ikke er opprettett, så både karakteren og faget opprettes
    if fag in emneliste:
        k = godkjent_karakter(input('Karakter (<enter> for å slette): '))
        if k is 'SLETT':
            karakterer.pop(fag)
        else:
            karakterer[fag] = k

    elif fag is not None:
        a = input('Trykk <enter> om du vil legge til emne i lista.')
        if a is '':
            emneliste.append(fag)
        else:
            return None
    else:
        print('Velg et fag som eksisterer eller opprett faget som et nytt gyldig emne!\n')

def emnelista(fag): #Sted med ulike lister for ulike fagkoder
    global karakterer, emneliste, d, liste, samling_alt
    samling_alt = karakterer
    for element in emneliste:
        if element not in samling_alt:
            samling_alt[element] = '' #Litt usikker om denne funker.. Den skal lage en ny dict. som har fag med og uten karakterer
    if fag is 'rumpe':
        for r in sorted(samling_alt):
            print(r, samling_alt[r])
    elif fag is '':
        b = input('Nivå (1, 2 eller 3. <enter> for alle):')
        if b == '':
            for j in sorted(samling_alt):
                if d == '4':
                    liste.append(samling_alt[j])
                else:
                    print(j, samling_alt[j])
        elif b.upper() == '1':
            for x in sorted(samling_alt):
                if x[-3] == '1':
                    if d == '4':
                        liste.append(samling_alt[x])
                    else:
                        print (x, samling_alt[x])
        elif b.upper() == '2':
            for y in sorted(samling_alt):
                if y[-3] == '2':
                    if d == '4':
                        liste.append(samling_alt[y])
                    else:
                        print (y, samling_alt[y])
        elif b.upper() == '3':
            for z in sorted(samling_alt):
                if z[-3] == '3':
                    if d == '4':
                        liste.append(samling_alt[z])
                    else:
                        print (z, samling_alt[z])
        else:
            print('prøv på nytt')

    elif fag.upper() == 'ØKONOMI':
        nivå_ø = input('Nivå (1, 2 eller 3. <enter> for alle):')
        for økofag in sorted(samling_alt):
            if 'ECON' in økofag:
                if nivå_ø == '':
                    if d == '4':
                        liste.append(samling_alt[økofag])
                    else:
                        print(økofag, samling_alt[økofag])
                elif nivå_ø == '1':
                    if økofag[-3] == '1':
                        if d == '4':
                            liste.append(samling_alt[økofag])
                        else:
                            print (økofag, samling_alt[økofag])
                elif nivå_ø == '2':
                        if økofag[-3] == '2':
                            if d == '4':
                                liste.append(samling_alt[økofag])
                            else:
                                print (økofag, samling_alt[økofag])
                elif nivå_ø == '3':
                        if økofag[-3] == '3':
                            if d == '4':
                                liste.append(samling_alt[økofag])
                            else:
                                print (økofag, samling_alt[økofag])
                else:
                    print('prøv på nytt')

    elif fag.upper() == 'INFORMATIKK':
        nivå_i = input('Nivå (1, 2 eller 3. <enter> for alle):')
        for infofag in sorted(samling_alt):
            if 'INFO' in infofag:
                if nivå_i == '':
                    if d == '4':
                        liste.append(samling_alt[infofag])
                    else:
                        print(infofag, samling_alt[infofag])
                elif nivå_i == '1':
                    if infofag[-3] == '1':
                        if d == '4':
                            liste.append(samling_alt[infofag])
                        else:
                            print(infofag, samling_alt[infofag])
                elif nivå_i == '2':
                    if infofag[-3] == '2':
                        if d == '4':
                            liste.append(samling_alt[infofag])
                        else:
                            print(infofag, samling_alt[infofag])
                elif nivå_i == '3':
                    if infofag[-3] == '3':
                        if d == '4':
                            liste.append(samling_alt[infofag])
                        else:
                            print(infofag, samling_alt[infofag])
                else:
                    print('prøv på nytt')

    elif fag.upper() == 'GEOLOGI':
        nivå_g = input('Nivå (1, 2 eller 3. <enter> for alle): ')
        for geofag in sorted(samling_alt):
            if 'GEO' in geofag:
                if nivå_g == '':
                    if d == '4':
                        liste.append(samling_alt[geofag])
                    else:
                        print(geofag, samling_alt[geofag])
                elif nivå_g == '1':
                    if geofag[-3] == '1':
                        if d == '4':
                            liste.append(samling_alt[geofag])
                        else:
                            print(geofag, samling_alt[geofag])
                elif nivå_g == '2':
                    if geofag[-3] == '2':
                        if d == '4':
                            liste.append(samling_alt[geofag])
                        else:
                            print(geofag, samling_alt[geofag])
                elif nivå_g == '3':
                    if geofag[-3] == '3':
                        if d == '4':
                            liste.append(samling_alt[geofag])
                        else:
                            print(geofag, samling_alt[geofag])
                else:
                    print('prøv på nytt')

    else:
        nivå_ = input('Nivå (1, 2 eller 3. <enter> for alle):') #Med denne kan man få fram andre fag enn de tre hovedtypene jeg har valgt
        for andre_fag in sorted(samling_alt):
            if ('ECON' or 'INFO' or 'GEO') not in andre_fag:
                if nivå_ == '':
                    if d == '4':
                        liste.append(samling_alt[andre_fag])
                    else:
                        print(andre_fag, samling_alt[andre_fag])
                elif nivå_ == '1':
                    if andre_fag[-3] == '1':
                        if d == '4':
                            liste.append(samling_alt[andre_fag])
                        else:
                            print(andre_fag, samling_alt[andre_fag])
                elif nivå_ == '2':
                    if andre_fag[-3] == '2':
                        if d == '4':
                            liste.append(samling_alt[andre_fag])
                        else:
                            print(andre_fag, samling_alt[andre_fag])
                elif nivå_ == '3':
                    if andre_fag[-3] == '3':
                        if d == '4':
                            liste.append(samling_alt[andre_fag])
                        else:
                            print(andre_fag, samling_alt[andre_fag])
                else:
                    print('prøv på nytt')

def emne():
    global emneliste, karakterer
    a = emnelista(input('Velg fag og/eller emnenivå (<enter> for alle)\nFag: '))

def karaktersnitt():
    global liste
    liste = []
    sum = 0
    antall_karakterer = 0
    emnelista(input('Velg fag og/eller emnenivå (<enter> for alle)\nFag: '))
    for element in liste:
        if 'A' in element:
            sum += 5
            antall_karakterer += 1
        elif 'B' in element:
            sum += 4
            antall_karakterer += 1
        elif 'C' in element:
            sum += 3
            antall_karakterer += 1
        elif 'D' in element:
            sum += 2
            antall_karakterer += 1
        elif 'E' in element:
            sum += 1
            antall_karakterer += 1
        elif 'F' in element:
            sum += 0
            antall_karakterer += 1
    if antall_karakterer != 0:
        gjennomsnitt = sum / antall_karakterer
    else:
        gjennomsnitt = 100
    if gjennomsnitt < 0.5:
        print ('F')
    elif 0.5 <= gjennomsnitt < 1.5:
        print ('E')
    elif 1.5 <= gjennomsnitt < 2.5:
        print ('D')
    elif 2.5 <= gjennomsnitt < 3.5:
        print ('C')
    elif 3.5 <= gjennomsnitt < 4.5:
        print ('B')
    elif 4.5 <= gjennomsnitt <= 5:
        print ('A')
    else:
        print('Må ha noen karakterer å regne ut snittet på')

def lagre():
    global karakterer, emneliste
    with open('karakterfil.txt', 'w') as fil:
        fil.seek(0)
        fil.truncate(0)
        fil.write(str(karakterer))

    with open('emnefil.txt', 'w') as file:
        file.seek(0)
        file.truncate(0)
        file.write(str(emneliste))

def start():
    global emneliste, karakterer, d

    d = 0
    emnelista('rumpe')
    meny()

    ulike_valg = ['0','1','2','3','4','5','6']
    
    while True:

        d = input('Velg handling (0 for meny): ')
        if d.isnumeric() and d not in ulike_valg:
            print('Du må velge mellom 0 og 6')

        elif d == '0':
            meny()
        elif d == '1':
            emne()
        elif d == '2':
            e = godkjent_emne(input('Nytt emne: '))
            if e is not None:
                emneliste.append(e)
        elif d == '3':
            ny_karakter()
        elif d == '4':
            karaktersnitt()
        elif d == '5':
            end = input('Skriv hva som helst om du vil lagre endringene før du avslutter. <Enter> for å kun avslutte: ')
            if end != '':
                lagre()
                print('Programmet er lagret.\nAvslutter')
            else:
                print('Avslutter')
            break
        elif d == '6':
            lagre()
            print('Alle endringer er lagret')
        else:
            print('Ugyldig verdi!\n')



try:
    karakterer = eval(open('karakterfil.txt').read())
except:
    karakterer = {}
    print('Lagre for å opprette filene')

try:
    emneliste = eval(open('emnefil.txt').read())
except:
    emneliste = []

a = ['♣ A', '♥ 10', '♦ A', '♠ 10']
print(len(a))
start()

#b)
