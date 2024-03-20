# Pievienoju savu koda variantu:
import random 

class Node:
    def __init__(self, value, player1_points=0, player2_points=0):
        self.value = value
        self.children = []
        self.player1_points = player1_points
        self.player2_points = player2_points

def generate_tree(number, parent=None, player1_points=0, player2_points=0, current_player = 1):
    if number < 10:
        return



#    Iziet cauri visiem iespējamajiem dalītājiem (punktu pievienošanā gan ir neliela kļūda)

    for divisor in [2, 3, 4]:
        if number % divisor == 0:
            child_value = number // divisor
            if number % 2 == 0:
                if current_player == 1:
                    child_player1_points = player1_points
                    child_player2_points = player2_points - 1
                elif current_player == 2:
                    child_player1_points = player1_points - 1
                    child_player2_points = player2_points
            elif number % 2 != 0:
                if current_player == 1:
                    child_player1_points = player1_points + 1
                    child_player2_points = player2_points
                elif current_player == 2:
                    child_player1_points = player1_points
                    child_player2_points = player2_points + 1
            
            child_node = Node(child_value, child_player1_points, child_player2_points)
            parent.children.append(child_node)
            generate_tree(child_value, child_node, child_player1_points, child_player2_points, 2 if current_player == 1 else 1)

def print_tree(node, indent=0):
    print("  " * indent + f"{node.value} (Spēlētājs 1: {node.player1_points}, Dators: {node.player2_points})")
    for child in node.children:
        print_tree(child, indent + 1)

# Random skaitļu ģenerācija

def generate_numbers():
    numbers = []
    while len(numbers) < 5:
        number = random.randint(20000, 30000)
        if number % 2 == 0 and number % 3 == 0 and number % 4 == 0:
            numbers.append(number)
    return numbers
