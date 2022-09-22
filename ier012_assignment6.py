# Assignment 6

# Oppgave 1
# a) is the pre-order traversal

'''
class QuizGift():
    total_num_points = 0
    available_minutes = 100
    points = []
    minutes = []


    def __init__(self, capacity, points, minutes,n):
        self.capacity = capacity
        self.points = points
        self.minutes = minutes
        self.n = n



    def compute_result(self, capacity, minutes, points, n):

        if n == 0 or capacity == 0:
            return 0

        elif minutes[n - 1] > capacity:
            return QuizGift.compute_result(self, capacity, minutes, points, n -1)

        else:
            tmp1 = QuizGift.compute_result(self, capacity, minutes, points, n -1)
            tmp2 = minutes[n -1] + QuizGift.compute_result((self, capacity - minutes[n-1], minutes, points, n-1))

            return max(tmp1, tmp2)


    def print_result(self):
        QuizGift.total_num_points = QuizGift.compute_result(self, self.capacity, self.minutes, self.points, self.n)
        if QuizGift.total_num_points == 250:
            print('Sara won a watch')
        elif 750 > QuizGift.total_num_points > 250:
            print('Sara won a smartphone')
        elif 750 < QuizGift.total_num_points:
            print('Sara won a laptop')


item_weights = [15,20,40,50,20,10]
items_values = [120,200,150,350,100,90]
qg = QuizGift

sara = qg(100, item_weights, items_values, len(items_values))

sara.print_result()
'''
import math


class Shape():
    def __init__(self, length, side_b=None, side_c=None):
        self.length = length
        self.side_b = side_b
        self.side_c = side_c

    def compute_area(self):
        pass


class Square(Shape):
    def compute_area(self):
        return self.length ** 2


class Circle(Shape):
    def compute_area(self):
        return math.pi * self.length ** 2


class Triangle(Shape):
    def compute_area(self):
        s = (self.length + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.length) * (s - self.side_b) * (s - self.side_c))


my_square = Square(2)
my_circle = Circle(3.5)
my_triangle = Triangle(5, 4, 3)

print('The areas of our square, circle and triangle are:', my_square.compute_area(), my_circle.compute_area(),
      my_triangle.compute_area())


class House():
    count = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        profit = (self.price - self.cost)
        print('The profit of selling the house is...', str(profit) + '$')

    def change_price(self, new_price):
        if self.sold:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost = (self.cost + expense)
        self.condition = new_condition
        print('The house is renovated')

    def print_info(self):
        print('The owner of the house:', self.owner, '\nThe condition:', self.condition,
              '\nThe current price of the house:', str(self.price) + '$', '\nThe cost of the house:', str(self.cost) + '$')


house1 = House('Simon', 'Brand new', 1200000)
house2 = House('Ingrid', 'Old', 300000)

house1.renovate(70000, 'Luxurious')
house1.sell('Isak')

house1.print_info()
house2.print_info()
print('Total number of houses:', House.count)