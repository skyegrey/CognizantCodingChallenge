import random


from generate_initial_population import generate_initial_population
from score_population import score_individual, score_population
from crossover import crossover
from mutate import mutate


def main(population_size=500, crossover_chance=.3, mutation_chance=.1, generations=100):
    new_population = generate_initial_population(population_size)

    for generation_index in range(generations):
        sorted_population = sorted(new_population, key=lambda individual: score_individual(individual))
        print(f'{generation_index} best score: {score_individual(sorted_population[0])}. '
              f'Arrangement: {sorted_population[0]}')

        new_population = []
        replacement_chance = 1 - crossover_chance - mutation_chance
        count_replacement = round(replacement_chance * population_size)
        count_crossover = round(crossover_chance * population_size)
        count_mutate = round(mutation_chance * population_size)

        # Replace individuals
        new_population.extend(sorted_population[:count_replacement])

        def get_half_norm_sample():
            random.seed()
            # Roughly half norm -- easier than doing a lot of math :)
            index = int(min(abs(random.gauss(0, 1) * population_size / 3), population_size - 1))
            return sorted_population[index]

        # Crossover individuals
        for _ in range(count_crossover):
            parent_1 = get_half_norm_sample()
            parent_2 = get_half_norm_sample()
            new_population.append(crossover(parent_1, parent_2))

        for _ in range(count_mutate):
            individual = get_half_norm_sample()
            new_population.append(mutate(individual))
    else:
        sorted_population = sorted(new_population, key=lambda individual: score_individual(individual))
        print(f'Best Candidate: {sorted_population[0]} with collisions: {score_individual(sorted_population[0])}')


main()