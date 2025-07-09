from base.individuals import *

def create_population(pop_size):
    """Creates a population of individuals.

    Args:
        population_size (int): The desired size of the population.

    Returns:
        list: A list containing the created individuals.

    """
    return [create_individuals() for _ in range(pop_size)]



def calculate_population_gain(pop,gain_matrix):
    """Calculates the gain for each individual in the population.

    Args:
        population (list): A list of individuals.
        gain_matrix (list of lists) : A matrix containing gain values used to calculate the gain for each individual

    Returns:
        list: A list of gain values corresponding to each individual in the population.

    """
    return [calculate_route_gain(ind,gain_matrix) for ind in pop]














































