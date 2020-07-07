from random import randint


def generate_initial_population(population_size, sequence_length=8):
    return [[randint(0, sequence_length - 1) for _ in range(sequence_length)] for _ in range(population_size)]