liste = [5,2,3,4,0,1]

def selection_sort_one_pass(list):
    mini = list.index(min(list))
    #min = find_min(list)
    temp = list[0]
    list[0] = list[mini]
    list[mini] = temp
    return list
'''
def find_min(list):
    min = list[0]
    loc_min = 0
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
            loc_min = i
    return loc_min'''

print(selection_sort_one_pass(liste))

def one_pass(liste, index):
    sub_liste = liste[index:]
    smallest = min(sub_liste)

    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]

    if len(sub_liste) > 1:
        one_pass(liste, index+1)

    return liste

liste = [-4,0,1,9,0]
print(one_pass(liste,0))

def fac_rec(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    return number * fac_rec(number-1)
fac_rec(5)

def treunctuation(key):
    hash_value = ""
    i = 1
    for char in str(key):
        if i % 3 == 0 or i % 5 == 0:
            hash_value += char
        i += 1
    return hash_value

print(treunctuation(94283641911))