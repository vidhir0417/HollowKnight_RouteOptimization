import csv
import numpy as np
from copy import deepcopy
from base.individuals import *
import matplotlib.pyplot as plt
from algorithm.utils import * 


def ga(initializer,
       gain_matrix,
       evaluator,
       selector,
       crossover,
       mutator,
       pop_size, n_gens, p_xo, p_m, elite_func, verbose=False, maximization=True,
       log_path=None, elitism=True, seed=0, fit_plot=True):
    """
    Implements a genetic algorithm to provide an optimized route

    Args:
        initializer (function) : generates an initial population of individuals
        gain_matrix (list of lists) : data matrix cointaining the gain of each location to be used 
        evaluator (function) : evaluates the gain of the population of individuals
        selector (function) : selects an individual from the population based on their gain
        crossover (function) : performs a crossover technique on two parents to generate offspring
        mutator (function) : performs a mutation technique on an individual to  establish genetic diversity
        pop_size (int) : population size
        n_gens (int) : number of generations the ga runs for
        p_xo (float) : probability of crossover
        p_m (float): probability of mutation
        elite_func (function) : returns the elite individual and its fitness from the population
        verbose (bool) : If True, print the generation results into a csv file
        maximization (bool) : If True, maximize the gain function
        log_path (str) : path to a log file to save the generation results
        elitism (bool) : if True, use elitism to preserve the best individual in each generation
        seed(int) : for the random number generator
        fit_plot (boolean) : If True, returns a line plot with the best fitnesses of the generations

    Returns:
        population (list) :  final population of individuals
        pop_fit (list) : gains of the final population of individuals

    Raises:
        Exception : if the elite function is not provided
    """

    # Getting up the seed
    random.seed(seed)
    np.random.seed(seed)

    if elite_func is None:
        raise Exception('Without a proper elite function, I cannot work. Humph! *grumpy sounds*')

    # Initializing the gen 0 population:
    population = initializer(pop_size)
    # Evaluating the current population:
    pop_fit = evaluator(population, gain_matrix)

    # Track the best individual and fitness values over generations
    best_individuals = []
    best_fitnesses = [max(pop_fit)]

    for gen in range(n_gens):

        # Creating an empty offspring population:
        offspring = []

        # While the offspring population is not full:
        while len(offspring) < len(population):

            # Selecting different the parents
            p1 = selector(population, pop_fit)
            p2 = selector(population, pop_fit)

            counter = 0
            while p1 == p2 and counter < 10:
                counter += 1
                p1 = selector(population, pop_fit)
                p2 = selector(population, pop_fit)

            max_crossover_attempts = 40
            for attempt in range(max_crossover_attempts):
                if random.random() < p_xo:
                    # Xover
                    o1, o2 = crossover(p1, p2)
                else:
                    # Reproduction
                    o1, o2 = deepcopy(p1), deepcopy(p2)

                if random.random() < p_m:
                    # Mutating the offspring
                    o1, o2 = mutator(o1, p_m), mutator(o2, p_m)

                if no_constraint(o1) and no_constraint(o2):
                    # Adding the offspring into the offspring population
                    offspring.extend([o1, o2])
                    break  # Exit the while loop if valid offspring are generated

        # Making sure offspring population doesn't exceed pop_size
        while len(offspring) > pop_size:  # has to be before elitism
            offspring.pop()

        # If elitism, make sure the elite of the population is inserted into the next generation
        if elitism:
            elite, best_fit = elite_func(population, pop_fit)
            offspring[-1] = elite  # Adding the elite, unchanged into the offspring population

        # Replacing the current population with the offspring population
        population = offspring

        # Evaluating the current population:
        pop_fit = evaluator(population, gain_matrix)

        # Track the best individual and fitness values over generations
        new_elite, new_fit = elite_func(population, pop_fit)
        best_individuals.append(new_elite)
        best_fitnesses.append(new_fit)

        if verbose:
            if maximization:
                print(f'       {gen}       |        {new_fit}      ')
                print('-' * 32)

        if log_path is not None:
            with open(log_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([seed, gen, new_fit, new_elite])

    # Plot the best fitness over generations
    if fit_plot:
        plt.plot(range(0, n_gens + 1), best_fitnesses)
        plt.xlabel('Generation')
        plt.xticks(range(n_gens + 1))
        plt.ylabel('Fitness')
        plt.title('Best Fitness Over Generations')
        plt.show()

    best_ind = population[np.argmax(pop_fit)]
    best_fit = max(pop_fit)

    return best_ind, best_fit


