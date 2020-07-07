import random


def crossover(parent_1, parent_2):
    random.seed()
    crossover_point = random.randint(1, len(parent_1) - 2)
    return parent_1[:crossover_point] + parent_2[crossover_point:]