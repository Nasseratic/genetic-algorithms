import random as random


def select_chromosome( POINTS ,  DEGREE = 3 , GEN_MAX = 200 , POP_SIZE = 70):
    chromosome_len = DEGREE+1
    def get_total_benefit(items):
        total_benefit = 0.0
        for item in items:
            total_benefit += item.benefit
        return total_benefit

    def fitness(individual):
        #Compute the fitness of individual
        mse = 0
        for point in POINTS :
            for power in range(0,chromosome_len):
                fx = ( individual[power] * (point.x ** power) )   
            mse =+ ( ( fx - point.y ) ** 2 )
        return mse

    def generate_starting_population(POP_SIZE):
        return [generate_individual() for x in range (0,POP_SIZE)]

    def generate_individual():
        return [random.uniform( -10.0 , 10.0 ) for x in range (0,len(chromosome_len))]

    def none_uniform_mutate(target):
        # TODO
        # non-uniform mutation
        return 0

    def GA(population,  prop_of_crossover = 0.2, prop_of_mutation = 0.08, prop_of_survival = 0.05):
        parent_length = int(prop_of_crossover*len(population))
        survivals = population[len(population) - parent_length:]
        nonparents = population[: len(population) - parent_length]

        # Parent selection!
        for np in nonparents:
            if prop_of_survival > random.random():
                survivals.append(np)

        # parents mutation
        for p in survivals:
            if prop_of_mutation > random.random():
                mutate(p)

        # Produce offsprings
        offsprings = []
        desired_length = len(population) - len(survivals)
        while len(offsprings) < desired_length :
            parent1 = population[random.randint(0,len(survivals)-1)]
            parent2 = population[random.randint(0,len(survivals)-1)]        
            half = len(parent1)/2
            offspring = parent1[:half] + parent2[half:] #crossover
            if prop_of_mutation > random.random():
                mutate(offspring)
            offsprings.append(offspring)

        new_population = survivals
        new_population.extend(offsprings)
        return new_population

    generation = 1
    population = generate_starting_population(POP_SIZE)
    for g in range(0,GEN_MAX):
        population = sorted(population, key=lambda x: fitness(x), reverse=False)
        population = GA(population)
        generation += 1
    population = sorted(population, key=lambda x: fitness(x), reverse=False)
    return population[0]
