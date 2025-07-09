from base.individuals import *
from base.population import *
from base.data import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm.algorithm import *
from algorithm.utils import *

if __name__ == '__main__':
    
    
   #replace with wanted matrix

    data =  [[0, 506.1, -298.1, 63.7, 845.6, 879.4, 794.1, 117.8, 645.6, -183.7],
             [93.0, 0, 351.1, -264.0, -239.0, 649.8, 658.5, 471.8,-137.8, 860.8],
             [-256.5, 7.9, 0, 197.8, 741.5, 697.5, 23.8, -113.8, -285.8, 862.5],
             [703.1, 121.4, 387.4, 0, -9.3, 322.5, 8.7, 135.5, 251.0, 668.8],
             [864.5, 762.7, -95.3, 509.2, 0, -194.7, 572.9, 330.8, 8.2, -167.3],
             [385.9, 106.8, 860.1, 481.0, -271.4, 0, 322.9, -23.9, 262.1, 64.5],
             [217.0, 760.2, 647.8, -36.8, 474.7, 565.2, 0, 17.6, -201.2, 135.1],
             [723.8, 551.0, 851.7, 600.0, 62.5, 125.8, 18.8, 0, 98.6, 556.4],
             [729.6, 63.5, 609.1, 662.3, 613.7, 830.0, 400.0, 463.2, 0, 784.3],
             [-107.5, 621.5, 676.0, 123.7, -164.9, 892.2, 766.1, 524.6, 165.2, 0]]

    ga(create_population,
       data,
       calculate_population_gain,
       roulette_selection_max,
       cycle_crossover,
       displacement_mutation,
       150,
       15,
       0.8,
       0.1,
       get_elite_max ,
       False,
       True,
       'log/test_log.csv',
       False,
       12,
       True)


# Best Individual Obtained

#replace with obtained best individual 
best_ind = [1, 9, 6, 3, 5, 7, 2, 10, 8, 4, 1]

area_map= {'Skip KS':0, 'D': 1, 'FC': 2, 'G': 3, 'QS': 4, 'QG': 5, 'CS': 6, 'KS': 7, 'RG': 8, 'DV': 9, 'SN': 10}

route = nums_to_initials(best_ind , area_map)

print(f'Best solution is {route} route.')
