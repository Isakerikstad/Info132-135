#Oppgave 1
import math

#a
x =  171476

g = 'persiske'
def utskrift(g,x):
    print(f'Den {g} ordboken bruker {math.ceil(math.log(x,2))} steg.')
#b
utskrift(g,x)
x = 1100373
g = 'engelske'
utskrift(g,x)
#c
x = 260000
g = 'kinesiske'
utskrift(g,x)

#Oppgave 2
class Student:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def greeting(self):
        print('Hi, my name is', self.name)
        print('I am', self.age, 'years old')
        print('I am from', self.nationality)

student1 = Student('Sara',19,'Norway')
student1.greeting()

#Oppgave 3

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def legg_til_fremst(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print('Listen er tom')
            return

        iterator = self.head
        streng = ''

        while iterator:
            streng += str(iterator.data) + '-->'
            iterator = iterator.next

        print(streng)


node1 = Node('Ulriki')
node2 = Node('Leoni')
node3 = Node('Ami')

l = LinkedList()

l.head = node1
l.head.next = node2
l.head.next.next = node3

l.legg_til_fremst('Sondre')
l.legg_til_fremst('Isak')
l.print_list()

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

my_list = [1,2,3,4,5]

def reverse_list(my_list):
    stack = Stack()
    for e in my_list:
        stack.push(e)
    reversed_list = list(reversed(stack.__dict__['items']))
    return reversed_list

print(reverse_list(my_list))

