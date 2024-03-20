from functions import *
from timeit import default_timer as timer

# Tests number generating functions

time1 = timer()

numbers1 = generate_numbers()
print(numbers1)

numbers2 = generate_numbers2()
print(numbers2)

print('time taken to generate both arrays: ' + str(timer()-time1))




# test

tree = GenerateTree(26820)
tree.print_tree()
