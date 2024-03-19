import random

def generate_numbers():
    numbers = []
    num = 20004
    while num <= 30000:
        numbers.append(num)
        num += 12
<<<<<<< Updated upstream
    return random.sample(numbers, 5)
=======
    return random.sample(numbers, 5)

# klase GameNode
# satur skaitli, kas rodas dalot, punktu skaitu, ko iegūst spēlētājs
# un heiristiko novērtējumu 

'''class GameNodeData:
    def __init__(self, number, points, value):
        self.number = number
        self.points = points
        self.value = value

    def __str__(self):
        # prins in 3 rows, uncomment to change
        # return f"number = {self.number}\npoints = {self.points}\nvalue = {self.value}"
        
        # prints in one row
        return f"nr. = {self.number}, p. = {self.points}, v = {self.value}"
        '''

# ternary tree node

class TreeNode:
    def __init__(self, number, p1_points=0, p2_points=0):
        self.number = number
        self.children = []
        self.parent = None
        self.p1_points = p1_points
        self.p2_points = p2_points
        self.minmax_value = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def initialize_minmax_value(self):
        self.minmax_value = self.p1_points - self.p2_points
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = self.get_level() * '    '
        print(str(self.get_level()) + spaces + '|__' + str(self.number) + ', points & value: ' + str(self.p1_points) + ' ' + str(self.p2_points) + ', ' + str(self.minmax_value))
        if len(self.children) > 0:              # var arī if self.children
            for child in self.children:
                child.print_tree()


# ģenerē spēles koku no noteikta skaitļa
def GenerateTree(number, player1=0, player2=0):
    
    if number <= 10:
        return None
    
    root = TreeNode(number, player1, player2)

    for divisor in [2, 3, 4]:
        if number % divisor == 0:

            newNumber = number // divisor

            child_player1 = player1 + 1
            child_player2 = player2 + 1

            root.p1_points = player1
            root.p2_points = player2

            child = GenerateTree(newNumber, child_player1, child_player2)
            root.add_child(child)

    return root        
    
    '''
    if number % 2 == 0:
        
        newNumber = number // 2
        
        # loģika punktu un heiristiskā vērtējuma ģenerēšanai
        # newPoints = ...
        # newValue = ...

        child_2 = GenerateTree(newNumber)
        root.add_child(child_2)

    if number % 3 == 0:

        newNumber = number // 3

        child_3 = GenerateTree(newNumber)
        root.add_child(child_3)

    if number % 4 == 0:

        newNumber = number // 4

        child_4 = GenerateTree(newNumber)
        root.add_child(child_4)

    return root
    '''

# Pievienoju savu koda variantu:#
#
# class Node:
#    def __init__(self, value, player1_points=0, player2_points=0):
#        self.value = value
#        self.children = []
#        self.player1_points = player1_points
#        self.player2_points = player2_points
#
# def generate_tree(number, parent=None, player1_points=0, player2_points=0, current_player = 1):
#   if number < 10:
#        return
#
#    Iziet cauri visiem iespējamajiem dalītājiem (punktu pievienošanā gan ir neliela kļūda)
#
#    for divisor in [2, 3, 4]:
#        if number % divisor == 0:
#            child_value = number // divisor
#            if number % 2 == 0:
#                if current_player == 1:
#                    child_player1_points = player1_points
#                    child_player2_points = player2_points - 1
#                elif current_player == 2:
#                    child_player1_points = player1_points - 1
#                    child_player2_points = player2_points
#            elif number % 2 != 0:
#                if current_player == 1:
#                    child_player1_points = player1_points + 1
#                    child_player2_points = player2_points
#                elif current_player == 2:
#                    child_player1_points = player1_points
#                    child_player2_points = player2_points + 1
#            
#            child_node = Node(child_value, child_player1_points, child_player2_points)
#            parent.children.append(child_node)
#            generate_tree(child_value, child_node, child_player1_points, child_player2_points, 2 if current_player == 1 else 1)
#
# def print_tree(node, indent=0):
#    print("  " * indent + f"{node.value} (Spēlētājs 1: {node.player1_points}, Dators: {node.player2_points})")
#    for child in node.children:
#        print_tree(child, indent + 1)

# Random skaitļu ģenerācija

def generate_numbers2():
    numbers = []
    while len(numbers) < 5:
        number = random.randint(20000, 30000)
        if number % 2 == 0 and number % 3 == 0 and number % 4 == 0:
            numbers.append(number)
    return numbers

>>>>>>> Stashed changes
