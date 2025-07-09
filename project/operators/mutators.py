from base.individuals import *
import random


def swap_mutation(individual, p_m):
    """
    Applies swap mutation to the individual with a given probability.

    Args:
        individual (list): The individual to mutate.
        p_m (float): The probability of mutation.

    Returns:
        list: The mutated individual.
    """
    
    # Exclude start and end point from mutation process
    mutated_individual = pre_operations(individual.copy())
    
    if random.random() < p_m:
        first_index, second_index = random.sample(range(len(mutated_individual)), 2)
        
        # Perform mutation by swapping the current gene with a random gene
        mutated_individual[first_index],mutated_individual[second_index]= mutated_individual[second_index], mutated_individual[first_index]

    # Add start and end point (D) to the mutated individual
    mutated_individual = post_operations(mutated_individual)

    # Fix potential cases for placeholder
    return fix_placeholder(mutated_individual)




def inversion_mutation(individual, p_m):
    """
    Applies inversion mutation to the individual with a given probability.

    Args:
        individual (list): The individual to mutate.
        p_m (float): The probability of mutation.

    Returns:
        list: The mutated individual.
    """

    # Exclude start and end point from mutation process
    mutated_individual = pre_operations(individual.copy())
   
    if random.random() < p_m:

        # Select a random segment to invert
        start_index, end_index = random.sample(range(len(mutated_individual)), 2)

        if start_index > end_index:
            end_index, start_index = start_index, end_index
                
        # Perform inversion
        mutated_individual[start_index:end_index] = reversed(mutated_individual[start_index:end_index])
        
    # Add start and end point (D) to the mutated individual
    mutated_individual = post_operations(mutated_individual)

    # Fix potential cases for placeholder
    return fix_placeholder(mutated_individual)


            

def scramble_mutation(individual, p_m):
    """
    Applies scramble mutation to the individual with a given probability.

    Args:
        individual (list): The individual to mutate.
        p_m (float): The probability of mutation.

    Returns:
        list: The mutated individual.
    """

    # Exclude start and end point from mutation process
    mutated_individual = pre_operations(individual.copy())

    if random.random() < p_m:

        # Select a random segment to scramble
        start_index, end_index = random.sample(range(len(mutated_individual)), 2)

        if start_index > end_index:
            end_index, start_index = start_index, end_index

        # Perform scrambling
        segment = mutated_individual[start_index:end_index]

        random.shuffle(segment)

        mutated_individual[start_index:end_index] = segment
        
    # Add start and end point (D) to the mutated individual
    mutated_individual = post_operations(mutated_individual)

    # Fix potential cases for placeholder
    return fix_placeholder(mutated_individual)


def insertion_mutation(individual, p_m):
    """
    Applies insertion mutation to the individual with a given probability.

    Args:
        individual (list): The individual to mutate.
        p_m (float): The probability of mutation.

    Returns:
        list: The mutated individual.
    """

    # Exclude start and end point from mutation process
    mutated_individual = pre_operations(individual.copy())
    
    # Ensure mutated_individual has at least one gene
    if len(mutated_individual) <= 1:
        return mutated_individual

    if random.random() < p_m:

        # Select a random gene to remove
        gene_index = random.randint(0, len(mutated_individual) - 1)
        gene = mutated_individual.pop(gene_index)

        # Reinsert the gene at a random position
        insert_index = random.randint(0, len(mutated_individual)-1)
        mutated_individual.insert(insert_index, gene)
        
    # Add start and end point (D) to the mutated individual
    mutated_individual = post_operations(mutated_individual)

    # Fix potential cases for placeholder
    return fix_placeholder(mutated_individual)


def displacement_mutation(individual, p_m):
    """
    Perform displacement mutation on an individual with a given mutation probability.

    Parameters:
    individual (list): The individual to be mutated.
    p_m (float): The probability of mutation.

    Returns:
    list: The mutated individual
    """
    
    # Exclude start and end point from mutation process
    mutated_individual = pre_operations(individual.copy())

    if random.random() < p_m:

        # Select a random start index for the substring to displace
        start_index = random.randint(0, len(mutated_individual) - 1)

        # Select a random end index for the substring, ensuring it is after the start index
        end_index = random.randint(start_index, len(mutated_individual))

        # Select a random index where the displaced substring will be inserted
        insert_substring_index = random.randint(0, len(mutated_individual))
        

        # Extract the substring to be displaced
        substring_to_displace = mutated_individual[start_index:end_index]

        # Delete the substring from the original location
        del mutated_individual[start_index:end_index]

        # Insert the displaced substring at the new location
        mutated_individual[insert_substring_index:insert_substring_index] = substring_to_displace

    # Add start and end point (D) to the mutated individual
    mutated_individual = post_operations(mutated_individual)

    # Fix potential cases for placeholder
    return fix_placeholder(mutated_individual)



