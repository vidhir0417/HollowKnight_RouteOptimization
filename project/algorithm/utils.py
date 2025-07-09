import random
import numpy as np


def get_elite_max(population, pop_fit):
    """
    Gets the elite individual and its corresponding maximum gain value from a given population

    Args:
        population (list) : collection of individuals in the population
        pop_fit (list) : collection of gain values corresponding to each individual in the population

    Returns:
        list : containing the elite individual and its maximum gain value
    """
    return [population[np.argmax(pop_fit)], max(pop_fit)]


def get_n_elites(n):
    """
    Gets the top n elite individuals and their corresponding gain values from a given population

    Args:
        n (int) : number of elite individuals to get

    Returns:
        callable : a function that takes in a population and its corresponding gain values,
                    returning the top n elite individuals and their gain.
    """
    def get_elite(population, pop_fit):
        """
        Gets all the elite individuals and their corresponding gain values from a given population into a list.

        Args:
             population (list) : collection of individuals in the population
             pop_fit (list) : collection of gain values corresponding to each individual in the population

        Returns:
            list : containing all the elite individuals and their corresponding gain values
        """
        # Getting the best n elites
        bests_i = np.argsort(pop_fit)[-n:]
        # Getting the fitnesses of the best n elites:
        return [population[i] for i in bests_i], [pop_fit[i] for i in bests_i]
    return get_elite
