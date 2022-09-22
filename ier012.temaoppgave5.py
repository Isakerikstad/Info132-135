#Obligatorisk temaoppgave 5 Isak Erikstad


#Oppgave 1

def fak(x):

    for m in range(1,x):
        x *= m

    return(x)



def fak2(y):
    n = 1
    while 0 < y:
        n = y*n
        y -= 1
    return (n) 


#Oppgave 2

#a)

#kongerekke=[]

class Monark:

    
   
    def __init__ (self, navn, nasjon, år):
        #global kongerekke
        self.navn = navn
        self.nasjon = nasjon
        self.år = år
        self.etterfølger = None
        #a = navn + ' av ' + nasjon + ' tiltro i ' + str(år)
        #kongerekke.append(a)


        
    def _etterfølger(self, etterfølger):
        self.etterfølger = etterfølger
  
    
    def skriv_ut(self):
        print(self.navn, 'av', self.nasjon, 'tiltro i', + self.år)


    def kongerekke(self):
        konge = self
        self.skriv_ut()
        while konge.etterfølger:
            konge.etterfølger.skriv_ut()
            konge = konge.etterfølger
        
    
haakon = Monark('Kong Haakon VII','Norge', 1905)
olav = Monark('Kong Olav V','Norge', 1957)
harald = Monark('Kong Harald V','Norge', 1991)

haakon._etterfølger(olav)
olav._etterfølger(harald)

#haakon.skriv_ut()
#olav.skriv_ut()
#harald.skriv_ut()

haakon.kongerekke()

                          
#kongerekke.append(haakon)
#kongerekke.append(olav)
#kongerekke.append(harald)

#for konger in (kongerekke):
   #  konger.skriv()

#print(kongerekke)
#b)


    




    

