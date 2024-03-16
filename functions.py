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
        # prins in 3 rows, uncomment to change
        # return f"number = {self.number}\npoints = {self.points}\nvalue = {self.value}"
        
        # prints in one row
        return f"nr. = {self.number}, p. = {self.points}, v = {self.value}"

# ternary tree node

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = self.get_level() * '    '
        print(spaces + '|__' + str(self.data))
        if len(self.children) > 0:              # var arī if self.children
            for child in self.children:
                child.print_tree()

# ģenerē spēles koku no noteikta skaitļa

def GenerateTree(gameNodeData):
    
    number = gameNodeData.number
    if number <= 0:
        return None
    
    root = TreeNode(gameNodeData)

    if number % 2 == 0:
        
        newNumber = number // 2
        
        # loģika punktu un heiristiskā vērtējuma ģenerēšanai
        # newPoints = ...
        # newValue = ...

        child_2 = GenerateTree(GameNodeData(newNumber, gameNodeData.points, gameNodeData.value))
        root.add_child(child_2)

    if number % 3 == 0:

        newNumber = number // 3

        child_3 = GenerateTree(GameNodeData(newNumber, gameNodeData.points, gameNodeData.value))
        root.add_child(child_3)

    if number % 4 == 0:

        newNumber = number // 4

        child_4 = GenerateTree(GameNodeData(newNumber, gameNodeData.points, gameNodeData.value))
        root.add_child(child_4)

    return root
    

