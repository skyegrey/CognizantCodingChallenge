import random


def mutate(individual):
    random.seed()
    mutation_point = random.randint(0, len(individual) - 1)
    new_queen_position = random.randint(0, len(individual) - 1)
    mutated_individual = individual[:mutation_point] + [new_queen_position] + individual[mutation_point + 1:]
    return mutated_individual
