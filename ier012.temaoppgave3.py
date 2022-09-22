#Oppgave 1 a)

x=9
y=66

print(x!=7 and y<=50)
print((x>7 or 50<y) and (x>y or y<100))

#b)

print((not(x==7 or y>=50))==(x!=7 and y<=50))
print((not(x<7 and 50>y) or (x<y and y>100)) == (x>7 or 50<y) and (x>y or y<100))

#Oppgave 2

alder = int(input('Oppgi alder: '))
år_bosatt = int(input('Hvor lenge har du bodd i Tulleby? '))

if alder>=30 and år_bosatt>=9:
    print('Du kan bli ordfører eller sitte i bystyret.')

elif (30>alder>=25 and år_bosatt>=5) or (9>år_bosatt>=5 and alder>=25):
    print ('Du kan sitte i bystyret.')
    if 30-alder>=9-år_bosatt:
        x=30-alder
    else:
        x=9-år_bosatt
    print ('Prøv igjen om', x,'år for å bli ordfører.')  
    
elif alder<25 or år_bosatt<5:
    if 25-alder>=5-år_bosatt:
        x=25-alder
    else:
        x=5-år_bosatt
    print ('Du er ikke kvalifisert enda, prøv igjen om', x, 'år.')

#Oppgave 3

x=int(input('Tall: '))

if x>=10:
    print('Minst 10')
elif x<=5:
    print('Maks 5')
else:
    print('6, 7, 8 eller 9')
