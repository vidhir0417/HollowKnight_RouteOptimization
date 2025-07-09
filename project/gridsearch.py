from base.individuals import *
from base.population import *
from base.data import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm.algorithm import *
import random
import time
import csv
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from typing import *
import time
import multiprocessing
from itertools import product
import statistics as stat
import gc


def run_algorithm(args):
    algorithm, params = args
    start_time = time.time()
    best_ind,best_fit = algorithm(**params)
    end_time = time.time()
    run_time = end_time - start_time
    return best_fit, run_time


def grid_search(algorithm, n_runs, params_dict):
    """
    Perform a grid search over a given algorithm with different combinations of parameters.

    Args:
        algorithm (Callable): The algorithm function.
        n_runs (int): The number of times to run the algorithm for each parameter combination.
        params_dict (Dict[str, List[Any]]): A dictionary with parameter names as keys and a list of values for each parameter.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary containing the best performing combinations and their metrics.
    """

    # Creates a multiprocessing Pool with a number of processes equal to the number of CPU cores available on the computer
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Creating combinations
    keys = params_dict.keys()
    values = params_dict.values()
    combinations = list(product(*values))

    # Lists to store metrics
    model_combinations = []
    avg_runtime = []
    avg_fit = []

    print(f"With the parameters chosen, there will be {len(combinations)} combinations tested...\nStart:")

    comb = 0
    for combination in combinations:
        
        # Dictionary for the combination running
        params = dict(zip(keys, combination))
        model_combinations.append(params)

        # Lists for metrics of each iteration
        final_fits = []
        run_times = []
        
        # Finding combinations with the best metrics
        results = pool.map(run_algorithm, [(algorithm, params)] * n_runs)
        final_fits, run_times = zip(*results)

        avg_runtime.append(stat.mean(run_times))
        avg_fit.append(stat.mean(final_fits))
       
        comb += 1
        if comb % 5 == 0:
            print(f'{len(combinations) - comb} combinations left.')


    print('End!\nDone :)) Here are your final results:')

    fittest = model_combinations[avg_fit.index(max(avg_fit))]

    results = {'best_fit': {'model_parameters': fittest,
                           'time': avg_runtime[model_combinations.index(fittest)],
                           'avg_fit': avg_fit[model_combinations.index(fittest)]}}
    
    return results




data = generate_geo_matrix()

if __name__ == '__main__':
    result = grid_search(ga, 15, {'initializer': [create_population],
                                    'gain_matrix': [data],
                                    'evaluator': [calculate_population_gain],
                                    'selector': [roulette_selection_max, ranking_selection_max, tournament_selection_max,exponential_rank_selection,linear_rank_selection],
                                    'crossover': [cycle_crossover,pmx_crossover,
                                                         uniform_crossover,ox1_crossover],
                                    'mutator': [swap_mutation, inversion_mutation, scramble_mutation, insertion_mutation, displacement_mutation],
                                    'pop_size': [50,100,150],
                                    'n_gens': [5,15,20],
                                    'p_xo': [0.8, 0.9],
                                    'p_m': [0.2, 0.1],
                                    'elite_func': [get_elite_max],
                                    'verbose': [False],
                                    'maximization': [True],
                                    'log_path': [None],
                                    'elitism': [True,False],
                                    'seed': [12],
                                    'fit_plot': [None]})
    print(result)

