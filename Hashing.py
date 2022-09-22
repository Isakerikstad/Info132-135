import random
def h(key):
    p = 109345121
    a = random.randint(1,p)
    b = random.randint(1,p)
    m = 12000
    return ( (a*key + b) % p ) % m
print(h(2022))

class Employee:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

