import random

def generate_numbers():
    numbers = []
    num = 20004
    while num <= 30000:
        numbers.append(num)
        num += 12
    return random.sample(numbers, 5)