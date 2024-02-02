import numpy as np
def objective_function(x):
    return -x**2 + 4*x - 4

population_size=50
generations = 100
mutation_rate = 0.1
                                                                                                                                        
population  = np.random.uniform(-10,10 , size=population_size)
for generation in range(generations):
    fitness = objective_function(population)
    sorted_indicies = np.argsort(fitness)[::-1]
    selected_pop = population[sorted_indicies[:population_size]]

    crossover_pop = np.random.choice(selected_pop, size=population_size)
    mutation_mask = np.random.rand(population_size)<mutation_rate
    mutation_pop = np.random.uniform(-1,1,size=population_size)
    crossover_pop[mutation_mask]+=mutation_pop[mutation_mask]

    population= crossover_pop
best_individual = np.argmax(objective_function(population))
best_x=population[best_individual]
print(best_x)
print(objective_function(best_x))