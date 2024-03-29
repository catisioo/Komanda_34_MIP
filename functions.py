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

def generate_numbers2():
    numbers = []
    while len(numbers) < 5:
        number = random.randint(20000, 30000)
        if number % 2 == 0 and number % 3 == 0 and number % 4 == 0:
            numbers.append(number)
    return numbers


# ternary tree node

class TreeNode:
    def __init__(self, number, p1_points=0, p2_points=0, level=0, minmax_value=0):
        self.number = number
        self.children = []
        self.parent = None
        self.p1_points = p1_points
        self.p2_points = p2_points
        self.minmax_value = minmax_value
        self.level = level

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
        print(spaces + '|__' + str(self.number) + ', points: ' + str(self.p1_points) + '; ' + str(self.p2_points) + ' minmax val.: ' + str(self.minmax_value))
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

# generates game tree from number

def GenerateTree(number, player1=0, player2=0, node_level=0, minmax_value=0):
    
# parbaudei jabut beigas, nevis sakuma:    
#    if number <= 10:
#        return None
    
    root = TreeNode(number, player1, player2, node_level, minmax_value)



    for divisor in [2, 3, 4]:
        if number % divisor == 0:

            newNumber = number // divisor

            if node_level % 2 == 0:
                if newNumber % 2 == 0:
                    child_player2 = player2 - 1
                    child_player1 = player1
                else:
                    child_player1 = player1 + 1
                    child_player2 = player2
            
            else:
                if newNumber % 2 == 0:
                    child_player1 = player1 - 1
                    child_player2 = player2
                else:
                    child_player2 = player2 + 1
                    child_player1 = player1

            #debugging stuff:
            #print('root.get_lelvel: ' + str(root.get_level())) 
            #print('node_level: ' + str(node_level))

     

            child = GenerateTree(newNumber, child_player1, child_player2, node_level + 1, child_player1 - child_player2)
            root.add_child(child)

    return root        
    # parbaudei jabut beigas, nevis sakuma:
    if number <= 10:
        return None


