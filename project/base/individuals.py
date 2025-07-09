import random
from base.data import generate_geo_matrix


def no_constraint(areas):
    """
    Checks if a list of areas satisfies certain constraints.

    Args:
        areas (list): A list representing the visited areas.

    Returns:
        bool: True if the areas satisfy the constraints, False otherwise.
   """
    
    # Ensuring CS is not visited right after QG
    if 5 in areas and 6 in areas:
        cs_index = areas.index(6)
        qg_index = areas.index(5)

        if cs_index == qg_index + 1:
            return False
            
    # Ensure RG is in the last half
    if 8 in areas:
        rg_index = areas.index(8)
        if rg_index < len(areas) // 2:
            return False
        
    # Avoid having a repeated area (could happen after a crossover/mutation)   
    for area in areas[1:-1]:  
        if areas.count(area) > 1:
            return False

      
    return True


def create_individuals():
    """
    Create a random individual (route) represented as a list with random numbers from 2 to 10,
    ensuring it starts and ends at Dirtmouth (1). Return if it respects the constraints.

    Returns:
        list: A random individual.
    """
    
    while True:

        # Numbers from 2 to 10 representing areas
        areas = list(range(2, 11)) 
        random.shuffle(areas) 

        # Start at Dirtmouth (1)
        areas.insert(0, 1)  

        # End at Dirtmouth (1)
        areas.append(1)  
        
        if no_constraint(areas):
            return areas
        else:
            continue


def calculate_route_gain(individual, gain_matrix):
    """
    Calculate the gain of a given route (individual) based on the gain matrix.

    This function evaluates the total gain for a route represented by an individual.
    It accounts for specific conditions involving placeholders in the route and
    computes the gain both with and without these placeholders to determine the optimal
    route gain, and if changes to the individual are necessary.
   
    Args:
        individual (list): The individual array representing the route.
        gain_matrix (list of lists): Matrix representing gains between areas.

    Returns:
        float: The gain of the route.
    """

    gain_with_placeholder = 0
    gain_without_placeholder = 0
    areas = individual.copy() 
    
    if 4 in areas and 9 in areas:
        qs_index = areas.index(4)
        dv_index = areas.index(9)

        # Check if DV directly follows QS
        if dv_index == qs_index + 1: 

            # Check if KS is in the list
            if 7 in areas:  
                ks_index = areas.index(7)

                # Replace KS with a placeholder
                areas[ks_index] = 0  
        

    # Find the index of the placeholder if it exists
    placeholder_index = areas.index(0) if 0 in areas else None
    
    # Calculate gain for the route with placeholder
    if placeholder_index is not None:
        for i in range(len(areas) - 1):

            current_area = areas[i]
            next_area = areas[i + 1] 

            # If current area is a placeholder
            if current_area == 0 :  

            # Use the area before the placeholder
                current_area = areas[i - 1] 

            # If next area is a placeholder
            if next_area == 0 :  

                # Skip over the placeholder
                next_area = areas[i + 2] 

            gain_with_placeholder += gain_matrix[current_area - 1][next_area - 1]
                    
                              
    # Calculate gain for the route without the placeholder    
    for i in range(len(areas) - 1):

        # If individual has a placeholder, calculate it normally with KS back on it
        if placeholder_index is not None:
            areas[placeholder_index] = 7

        current_area = areas[i]
        next_area = areas[i + 1]

        gain_without_placeholder += gain_matrix[current_area - 1][next_area - 1]
    
    
    # If gain is bigger with a placeholder, then we replace in the actual individual KS for said placeholder 0 
    if gain_with_placeholder >= gain_without_placeholder and placeholder_index is not None:
        if 7 in individual: 

            ks_index = individual.index(7)
            individual[ks_index] = 0
        return gain_with_placeholder
    
    else:        
        return gain_without_placeholder



def nums_to_initials(individual, area_map):
    """
    Converts a list of area indices to their corresponding initials.

    Args:
        individual (list): The route represented by numeric indices.
        area_map (dict): A dictionary mapping area initials to their indices.

    Returns:
        list: A list of area initials representing the route.
    """

    idx_to_initial = {val: key for key, val in area_map.items()}
    return [idx_to_initial[area] for area in individual]



def pre_operations(individual):
    """
    Prepare the individual for genetic operations by removing the fixed start and end points (Dirtmouth).

    Args:
        individual (list): The individual representing a route.

    Returns:
        list: The individual with the start and end points (Dirtmouth) removed.
    """

    # Remove the first and last elements (Dirtmouth) for genetic processing
    return individual[1:-1]


def post_operations(modified_individual):
    """
    Restore the start and end points to the individual after genetic operations.

    Args:
        modified_individual (list): The modified individual without the start and end points.

    Returns:
        list: The individual with Dirtmouth reinserted at the start and end.
    """

    # Add Dirtmouth (D = 1) to the start and end of the route
    return [1] + modified_individual + [1]


def fix_placeholder(individual):
    """
    Fix the placeholder in a individual list, in the case its needed after a mutation or crossover.

    Args:
        individual (list): The individual route represented as a list.

    Returns:
        list: The individual route with the placeholder fixed, if necessary.
    """

    # Find the index of the placeholder (0) in the individual
    placeholder_index = individual.index(0) if 0 in individual else None

    if placeholder_index is not None:

        dv_index = individual.index(9) if 9 in individual else None
        qs_index = individual.index(4) if 4 in individual else None
        
        # KS should be placed back if DV does not directly follow QS
        if dv_index is not None and qs_index is not None and dv_index != qs_index + 1:

            # Replace placeholder with KS
            individual[placeholder_index] = 7  

    return individual





