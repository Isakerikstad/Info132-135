#Temaoppgave 8 Isak Erikstad
#a)

eksamen = {
    'INFO100': 'C', 'INFO104': 'B', 'INFO116': 'E',
    'INFO180': 'A', 'INFO201': 'F', 'INFO280': 'C',
    'GEO101': 'D', 'GEO110': 'B', 'ADM101': 'A',
    'ECON100': 'B', 'ECON201': 'C', 'GEO210': 'C',
    'FAIL101': 'F'
}

def karakterfrekvenser(dict):
    frekvens = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' :  0, 'F' : 0}
    for a in dict.values():
        if a == 'A':
            frekvens['A'] += 1
        elif a == 'B':
            frekvens['B'] += 1
        elif a == 'C':
            frekvens['C'] += 1
        elif a == 'D':
            frekvens['D'] += 1
        elif a == 'E':
            frekvens['E'] += 1
        elif a == 'F':
            frekvens['F'] += 1
    print(frekvens)
    return frekvens

a = karakterfrekvenser(eksamen)
a

#Oppgave b)

def histogram(frekvens):
    print('A', frekvens['A']*'*')
    print('B', frekvens['B'] * '*')
    print('C', frekvens['C'] * '*')
    print('D', frekvens['D'] * '*')
    print('E', frekvens['E'] * '*')
    print('F', frekvens['F'] * '*')

histogram(a)

#Oppgave 2A)
engelske_siffer = {
 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}
def sort(dictionary):
    for element in sorted(dictionary):
        if element in dictionary.keys():
            print(element,":", dictionary[element]) 
sort(engelske_siffer)

#Oppgave 2B)
def snu_fortegnelse(old_dict):
    new_dict = dict([(value, key) for key, value in old_dict.items()])
    print(new_dict)
    return new_dict

inv = snu_fortegnelse(engelske_siffer)
inv

#Oppgave 2C)

def sort_snu_fortegnelse(inv_dict):
    sorted_values = sorted(inv_dict.values())  # Sorterer verdiene
    sorted_dict = {}

    for i in sorted_values:
        for k in inv_dict.keys():
            if inv_dict[k] == i:
                sorted_dict[k] = inv_dict[k]
                break

    for element in sorted_dict:
        print(element, sorted_dict[element])

del engelske_siffer
sort_snu_fortegnelse(inv)



