#Temaoppgave 6 Isak Erikstad

#Oppgave 1

def sjekkvokal(a):
    #funksjon for å sjekke vokalene
    return a.lower() in ['a','e','i','o','u','y','æ','ø','å']

#returnerer antall vokaler i streng
def antallvokaler(str):
    try:
        antall = 0
        for u in range(len(str)):
            #sjekker for vokalen
            if sjekkvokal(str[u]):
                antall += 1
        return antall
    except Exeption:
         print(antall, '\nPrøv å skrive en tegnstreng')
        

#Oppgave 2
TV = '''\
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''

def verv(navn):
    liste = TV.split('\n')
    verv_person = []
    for verv in liste:
        if navn in verv:
            pos_verv = verv.find(': ')
            jobb = verv[0:pos_verv]
            verv_person.append(jobb)
    return verv_person

print(verv("Liv"))
