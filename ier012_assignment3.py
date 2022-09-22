#Oppgave 1
def hash_function(input_string, table_size):
    total = 0
    length = len(input_string)
    for pos in range(length):
        total = total + ord(input_string[pos]) + length
    return total % table_size

my_list = ['a1b2c3', 'CiTiBnk','232323','myLaptop']
my_choice = 19

for item in my_list:
    print(hash_function(item, my_choice), end=' ')

#Oppgave 2

import hashlib as hl
import random as ra
class HashClass():
    def __init__(self, id):
        self.id = self.hash_it(id)

    def hash_it(self, id):
        salt = ra.randint(1,1000)
        id += salt
        self.id = hl.sha1(str(id).encode()).hexdigest()
        return self.id

    def print_it(self):
        print(self.id)
        print(len(self.id))


my_hash = HashClass(11011999)
print('\n')
my_hash.print_it()

print(len('773030b9c773c67094447ea97855c7bccb469ad7'))

#oppgave 3

def sort_and_print(liste):
    name_dic = {}
    for name, budget in liste:
        name_dic[budget] = name
    sortert_liste = bubble_sort(list(name_dic.keys()))
    largest = max(sortert_liste)
    for element in liste:
        if largest in element:
            print('The movie with the largest budget is:\n', name_dic[largest])

def bubble_sort(arr):
    for pass_num in range(len(arr)-1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr
list_of_tuples = [('Birds of Prey', 97.1), ('Dolittle', 175.0), ('The Gentlemen', 7.0), ('Falling', 22.0)]
sort_and_print(list_of_tuples)


#Oppgave 4

def magic_function(element):
    if len(element) <= 1:
        yield element
    else:
        for e in magic_function(element[1:]):
            for i in range(len(element)):
                yield e[:i] + element[0:1] + e[i:]
result = []
for p in magic_function('abcd'):
    result.append(p)
print(result)
