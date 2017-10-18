import random as random

def get_total_benefit(items):
    total_benefit = 0
    for item in items:
        total_benefit += item.benefit
    return total_benefit
 
def select_chromosome( CAPACITY  , ITEMS , GEN_MAX = 200 , POP_SIZE = 70):

    def fitness(individual):
        #Compute the fitness of individual
        total_benefit = 0
        total_weight = 0
        index = 0
        for i in individual:        
            if index >= len(ITEMS):
                break
            if (i == 1):
                total_benefit += ITEMS[index].benefit
                total_weight += ITEMS[index].weight
            index += 1
            
        
        if total_weight > CAPACITY:
            return 0
        else:
            return total_benefit


    def generate_starting_population(POP_SIZE):
        return [generate_individual() for x in range (0,POP_SIZE)]

    def generate_individual():
        return [random.randint(0,1) for x in range (0,len(ITEMS))]



    def mutate(target):
        #Do mutation
        r = random.randint(0,len(target)-1)
        if target[r] == 1:
            target[r] = 0
        else:
            target[r] = 1


    # ---------------------------------------------

    def GA(population,  prop_of_survival = 0.2, prop_of_mutation = 0.08, prop_of_crossover = 0.05):
    

        parent_length = int(prop_of_survival*len(population))
        survivals = population[:parent_length]
        nonparents = population[parent_length:]

        # Parent selection!
        for np in nonparents:
            if prop_of_crossover > random.random():
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


    # -------------------------------

    generation = 1
    population = generate_starting_population(POP_SIZE)
    for g in range(0,GEN_MAX):
        #print "Generation %d with %d" % (generation,len(population))
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        # for i in population:        
        #     print "%s, fitness equal  %s" % (str(i), fitness(i))        
        population = GA(population)
        generation += 1
    return population[0]


def chromosome_to_items( items , chromosome):
    result = []
    for index, gene in enumerate(chromosome):
        if(gene == 1 ):
            result.append(items[index])
    return result