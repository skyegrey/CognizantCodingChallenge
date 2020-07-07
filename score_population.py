def score_population(population):
    return sum(score_individual(individual) for individual in population)


def score_individual(individual):
    collisions = 0

    for index in range(len(individual)):
        queen = individual[index]
        hittable_list = individual[index + 1:]
        for hittable_index in range(len(hittable_list)):
            hittable_queen = hittable_list[hittable_index]

            # Check for horizontal collision
            if queen == hittable_queen:
                collisions += 1

            # Check for positive diagonal collision
            elif (queen + hittable_index + 1) == hittable_queen:
                collisions += 1

            # Check for negative diagonal collision
            elif (queen - hittable_index - 1) == hittable_queen:
                collisions += 1
    return collisions
