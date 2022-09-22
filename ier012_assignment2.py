liste = [1001, 1030, 1050, 1020, 300, 1080, 1100]


def selection_sort(arr):
    x = 0
    for i in range(len(arr)):
        x += 1
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[minindex] > arr[j] :
                minindex = j
            arr[i], arr[minindex] = arr[minindex], arr[i]
        if x == 3:
            break
    return arr

print('Oppgave 1. This is what 3 passes of selection sort look like:',selection_sort(liste))
liste = [ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
def bubble_sort_3(arr):
    x = 0
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(pass_num):
            if x == 3:
                break
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
            x += 1
        return arr
print('Oppgave 2. This is what 3 passes of buble sort look like:', bubble_sort_3(liste))
def bubble_sort(array):
    antall = 0
    for pass_num in range(len(array)-1,0,-1):
        while antall < 3:
            antall+=1
            for i in range(pass_num):
                if array[i] > array[i+1]:
                    temp=array[i]
                    array[i]=array[i+1]
                    array[i+1]=temp


array2 = [ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]

bubble_sort(array2)
print("Sorted with bubble-sort:", array2,"\n")
def bubble_sort(arr):
    for pass_num in range(len(arr)-1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr
my_list = [5,4,3,2,1,2,3,4,5]

def sort_and_rem_dup(arr):
    sort = bubble_sort(arr)
    for i in range(len(sort)-1,0,-1):
        if sort[i] == sort[i-1]:
            sort.remove(sort[i])
    return sort

new_list = sort_and_rem_dup(my_list)
print('Oppgave 3:', new_list)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


def check_palindrome(string):
    stack = Stack()
    for character in string:
        stack.push(character)

    reversed_text = ''
    while not stack.is_empty():
        reversed_text = reversed_text + stack.pop()

    if string == reversed_text:
        print('The string is a palindrome.')
    else:
        print('The string is not a palindrome.')

print('Oppgave 4:')
(check_palindrome("civic"))