import random
import numpy as np

def roulette_selection_max(pop, fitnesses):

    """Perform roulette wheel selection to choose an individual from the population based on fitness for maximization.

    Args:
    pop (list): List of individuals.
    fitnesses (list): List of fitness values corresponding to each individual in the population.

    Returns:
    object: Selected individual based on the roulette wheel selection for maximization.
    """

    sum_of_fitnesses = sum(fitnesses)

    probabilities = [fitness / sum_of_fitnesses for fitness in fitnesses]

    return random.choices(pop, weights=probabilities)[0]


def ranking_selection_max(population, fitness):
    """
    Performs Ranking Selection to choose an individual from the population based on fitness for maximization.

    Args:
        population (list): List of individuals.
        fitness (list): List of fitness values corresponding to each individual in the population.

    Returns:
        object: Selected individual based on the ranking selection for maximization.
    """
    
    # Sort the population by fitness (ascending order)
    sorted_pairs = sorted(zip(population, fitness), key=lambda x: x[1], reverse=False)

    # Sort the population
    sorted_population, sorted_fitnesses = zip(*sorted_pairs)

    # Get the rank indices (1 for worst, 'N' for best)
    rank_fitnesses = list(range(1, len(sorted_population) + 1))

    # Perform roulette wheel selection based on the rank indices
    return roulette_selection_max(sorted_population, rank_fitnesses)

def tournament_selection_max(pop, fitnesses):
    """
    Perform tournament selection to choose an individual from the population based on fitness for maximization.

    Args:
        pop (list): List of individuals.
        fitnesses (list): List of fitness values corresponding to each individual in the population.

    Returns:
        object: Selected individual based on the tournament selection for maximization.
    """
    # Define the size of the tournament pool
    tournament_size = 3  

    # Randomly select indices for the tournament pool
    indices = random.sample(range(len(pop)), tournament_size)

    # Identify the index of the individual with the maximum fitness in the tournament pool
    max_index = max(indices, key=lambda idx: fitnesses[idx])

    # Return the individual corresponding to the maximum fitness
    return pop[max_index]



def exponential_rank_selection(population, fitness, rate=0.1):
    """
    Performs Exponential Rank Selection to choose an individual from the population based on fitness.

    Args:
        population(list): List of individuals.
        fitness(list): List of fitness values corresponding to each individual in the population.
        rate(float): Exponential rate parameter. 

    Return:
        object: Selected individual based on the exponantial rank selection.
    """

    # Sort the population by fitness (descending order)
    sorted_pairs = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)

    # Sort the population
    sorted_population, sorted_fitnesses = zip(*sorted_pairs)

    # Get the rank indices
    rank = np.arange(1, len(sorted_population) + 1)

    # Calculate selection probabilities 
    probability = np.exp(-rate * rank)
    probability /= probability.sum() # Normalize probabilities

    return random.choices(population, weights=probability)[0]


def linear_rank_selection(population, fitness):
    """
    Performs Linear Rank Selection to choose an individual from the population based on fitness.

    Args:
        population (list): List of individuals.
        fitness (list): List of fitness values corresponding to each individual in the population.

    Returns:
        object: Selected individual based on linear rank selection.
    """
    
    # Sort the population by fitness (descending order)
    sorted_pairs = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)
    sorted_population, _ = zip(*sorted_pairs)

    # Calculate selection probabilities linearly
    num_individuals = len(sorted_population)
    probability = [(num_individuals - i) / (num_individuals * (num_individuals + 1) / 2) for i in range(num_individuals)]

    return random.choices(sorted_population, weights=probability)[0]