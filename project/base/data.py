import random

def generate_geo_matrix():
    """
    Generate a 10x10 matrix representing Geo transitions between different areas.

    The matrix is initialized with Geo values for transitions between different areas. 
    Specific rules are applied to ensure a unique condition for the Geo gain from 
    Greenpath to Forgotten Crossroads.

    Returns:
        list: A 10x10 matrix with randomly generated Geo values for each transition.
              The value for the transition from Greenpath (G) to Forgotten Crossroads (FC) 
              is set to be 3.2% less than the minimum positive Geo gain of all other transitions.
    """
    # Create a 10x10 matrix initialized with None for later updates
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    
    # Randomly initialize Geo values for transitions between areas
    for i in range(10):
        for j in range(10):
            if i != j:  
                matrix[i][j] = round(random.uniform(-300, 900), 1) 

    # Specific condition for Geo gains from Greenpath (G = 3) to Forgotten Crossroads (FC = 2)
    # Areas numbers: D - 1, FC - 2, G - 3, QS - 4, QG - 5, CS - 6, KS - 7, RG - 8, DV - 9, SN - 10
    # Calculate the minimum positive Geo gain across all transitions
    min_positive_geo = min(filter(lambda x: x > 0, [matrix[i][j] for i in range(10) for j in range(10) if i != j and matrix[i][j] is not None]))
    # Set the Geo gain from G to FC to be 3.2% less than the minimum of all other positive Geo gains
    matrix[2][1] = round(min_positive_geo * 0.968, 1) 

    return matrix
