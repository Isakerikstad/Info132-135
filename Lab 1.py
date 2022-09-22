class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hils(self, venn):
        print('Hei, navnet mitt er ' + self.name, '. \nHei, hyggelig å møte deg ' + self.name + ' mitt navn er ' + venn.name)

p1 = Person('Bengt', 24)
p2 = Person('Vilde', 23)

p1.hils(p2)


class Employe:

    lønn = 10000

    def __init__(self, fornavn, etternavn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.lønn

    def get_fullname(self):
        return f"{self.fornavn} {self.etternavn}"

    def print_email(self):
        print(self.fornavn + self.etternavn + '@company.com')

    def øk_lønn(self, rate):
        self.lønn = self.lønn * (float(rate)+1)
        print('Din nye lønn er:', "{:,.2f} £".format(self.lønn))

e1 = Employe('Isak', 'Erikstad')

print(e1.get_fullname())
e1.print_email()
e1.øk_lønn(2.5)


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if str(guess) > str(item):
            high = mid - 1
        else:
             low = mid + 1
    return None

list = [23, 25, "ANTMAN", "BATMAN", "BEAST BOY", "CATWOMAN", "HAWKGIRL"]

print (binary_search(list, "HAWKGIRL"))