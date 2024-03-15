import random

# funkcija, kas ģenerē 5 skaitļus
# atgriež ARRAY ar 5 skaitļiem

def generate_numbers():
    numbers = []
    num = 20004
    while num <= 30000:
        numbers.append(num)
        num += 12
    return random.sample(numbers, 5)

# klase GameNode
# satur skaitli, kas rodas dalot, punktu skaitu, ko iegūst spēlētājs
# un heiristiko novērtējumu 

class GameNodeData:
    def __init__(self, number, points, value):
        self.number = number
        self.points = points
        self.value = value

    def __str__(self):
        return f"number = {self.number}\npoints = {self.points}\nvalue = {self.value}"

# ternary tree
    
class Node:
    def __init__(self, data):
        self.left = None
        self.middle = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)