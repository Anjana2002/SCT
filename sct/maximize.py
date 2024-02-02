# Write a program for Genetic algorithm to maximize the function f(x)=x2.
import numpy as np
def objective_function(x):
    return x**2

population_size = 100
generations = 100
mutation_rate = 0.1

#initialization
population = np.random.uniform(-10,10, size = population_size)

for generation in range(generations):
    # Evaluate the fitness of each individual in the population
    fitness = objective_function(population)

    # Select the top individuals based on fitness
    sorted_indices = np.argsort(fitness) [::-1]
    selected_pop = population[sorted_indices[:population_size]]

    # Crossover: Create new individuals by combining pairs of selected individuals
    crossover = np.random.choice(selected_pop, size= population_size)

    # Mutation: Introduce random changes to some individuals
    mutation_mask = np.random.rand(population_size) < mutation_rate
    mutation_pop = np.random.uniform(-1, 1, size = population_size)
    crossover[mutation_mask] +=mutation_pop[mutation_mask]

    # Replace the old population with the new one
    population = crossover

# Find the best individual in the final population
best_individual = np.argmax(objective_function(population))
best_x = population[best_individual]

print(f"Optimal x: {best_x}")
print(f"Optimal f(x): {objective_function(best_x)}")
