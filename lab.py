def fib(number):
    counter = 1
    a = 0
    print(a)
    b = 1
    while counter != number:
        print(a + b)
        a += b
        b = a - b
        counter += 1


def fibo(term):
    if term <= 1:
        return (term)
    else:
        return (fibo(term - 1) + fibo(term - 2))


# Change this value to adjust the number of terms in the sequence.
number_of_terms = 10
for i in range(number_of_terms):
    print(fibo(i))

N = 15
for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j - 1) == i):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


def a_space_classic(n):
    z = n - 1
    x = 1
    for i in range(n):
        for i in range(z):
            print('  ', end='')
        for i in range(x):
            print('+ ', end='')
        for i in range(z):
            print(' ', end='')
        x += 2
        z -= 1
        print()


a_space_classic(6)


def one_pass(liste, index):
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
    return liste


def selection_sort(liste):
    for i in range(len(liste)):
        one_pass(liste, i)
    return liste


liste = [2, 22, 23, 44, -4, 0, 1, 9, 0]


# print(selection_sort(liste))

def one_pass(liste):
    index = 0
    while index != len(liste):
        sub_liste = liste[index:]
        smallest = min(sub_liste)
        smallest_index = sub_liste.index(smallest) + index
        liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
        index += 1
    return liste


print(liste)
print(one_pass(liste))


# Expected output: [-4, 0, 0, 1, 9]

# Lab 6
# Exercise 1
def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num - 1)


print('Recur factorial',recur_factorial(100))


# Exercise 2
def truncation_hash(key):
    hash_value = ''
    counter = 0
    for num in str(key):
        counter += 1
        if counter % 3 == 0:
            hash_value += num
        elif counter % 5 == 0:
            hash_value += num
    return int(hash_value)


print(truncation_hash(94283641911))


def string_hash(key):
    hash_value = 1
    for char in key:
        hash_value *= ord(char)
    return hash_value


print(string_hash('heipådeg'))


# Exercise 3

class PasswordDatabase():
    passwords = {}

    def create_user(self):
        username = input('Choose your username')
        password = input('Choose your password')
        self.passwords[username] = hash(password)

    def check_password(self, username=None, password=None):
        if username is None and password is None:
            username = input('What is your username?')
            password = input('What is your password?')
        if username in self.passwords.keys():
            return self.passwords[username] == hash(password)
        else:
            print('Username incorrect')

    def update_password(self):
        username = input('What is your username?')
        password = input('What is your password?')
        if self.check_password(username, password) is True:
            password = input('Type in your new password')
            self.passwords[username] = hash(password)
            print('Password updated')
        else:
            print('Incorrect password')


p = PasswordDatabase()
p.create_user()

#Lab 7
graph = [('A','B'), ('A','C'), ('B','A'), ('C','A'), ('B','C')]

def remove_node(node, graph):
    new_graph = []
    for element in graph:
        if element[0] != node and element[1] != node:
            new_graph.append(element)
    return new_graph


class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        self.graph.setdefault(node, []).append(neighbour)
        self.graph.setdefault(neighbour, []).append(node)

    def get_neighbours(self, node):
        if node in self.graph:
            return self.graph[node]
        return []

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for element in self.graph:
                while node in self.graph[element]:
                    self.graph[element].remove(node)
        else:
            print('Node has already been removed.')

g = Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','A')
g.add_edge('C','A')
g.add_edge('B','C')

class Course:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def hash_it(self):
         return hash(f"{self.title}{self.year}")

my_course = Course('INFO125', 2019)
print(my_course.hash_it())

x = 2
if 4 > x > 1:
    print('Ja det g¨år')