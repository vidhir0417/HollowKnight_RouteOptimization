# Hollow Knight Route Optimization using Genetic Algorithms

This document details a project focused on applying genetic algorithms to solve a route optimization problem within the popular video game *Hollow Knight*.

## Purpose

The primary mission of this project was to create an algorithmic solution that optimizes a player's journey in *Hollow Knight*, ensuring **maximum Geo gains** while **reducing any losses**. This involves navigating 10 different game zones, starting and finishing at Dirtmouth's area, where each region presents opportunities for gains and risks of losses.

## Methodology

To address this optimization challenge, a **Genetic Algorithm (GA)**, a computational method inspired by natural selection and evolutionary biology, was employed.

The methodology involved:

* **Geo Matrix Generation:** Developed a `generate_geo_matrix` function to represent gain values for each game route, including a specific condition for Geo gains from Greenpath to Forgotten Crossroads.
* **Individual Creation:** A `create_individuals()` function generates random routes (lists of 11 values representing game areas), ensuring all routes begin and end in Dirtmouth.
* **Constraint Handling:** A `no_constraints` function validates individuals against specific game constraints (e.g., handling the QS-DV sequence).
* **Genetic Operators:**
    * **Selection:** Implemented and compared five different selection operators to choose parents based on fitness: `Roulette Selection`, `Ranking Selection`, `Tournament Selection`, `Exponential Rank Selection` and `Linear Rank Selection`.
    * **Crossover:** Implemented and compared four different crossover operators to combine genetic material from parents: `Cycle Crossover`, `Uniform Crossover`, `Partially Mapped Crossover (PMX)` and `Order Crossover (OX1)`.
    * **Mutation:** Implemented and compared five different mutation operators to introduce diversity: `Swap Mutation`, `Inversion Mutation`, `Scramble Mutation`, `Insertion Mutation` and `Displacement Mutation`.
* **Hyperparameter Optimization (Grid Search):** A key goal was to find the most optimal combination of GA parameters. A `grid_search` algorithm was developed to iterate over various combinations of `initializer`, `gain_matrix`, `evaluator`, `selector`, `crossover`, `mutator`, `pop_size`, `n_gens`, `p_xo` (probability of crossover), `p_m` (probability of mutation), `elite_func`, `verbose`, `maximization`, `log_path`, `elitism` and `seed`.

## Key Results

After extensive grid search (15 rounds), the following parameters were found to generate an individual with the best fitness:

* **Generations:** 15
* **Population Size:** 150
* **Selection Operator:** `Roulette Selection`
* **Mutation Operator:** `Displacement Mutation`
* **Crossover Operator:** `Cycle Crossover`
* **Probability of Crossover (`p_xo`):** 0.8
* **Probability of Mutation (`p_m`):** 0.1
* **Elitism:** False
* **Random Seed:** 12

The best route found yielded approximately **7098.8 Geo gains**.

* **Best Individual (Areas):** `[1, 9, 6, 3, 5, 7, 2, 10, 8, 4, 1]`
* **Best Solution (Route):** `['D', 'DV', 'CS', 'G', 'QG', 'KS', 'FC', 'SN', 'RG', 'QS', 'D']` (Dirtmouth, Distant Village, City Storerooms, Greenpath, Queen’s Gardens, King’s Station, Forgotten Crossroads, Stag Nest, Resting Grounds, Queen’s Station, Dirtmouth)

## Conclusion

This project successfully demonstrated the effectiveness of genetic algorithms in addressing complex optimization problems within a gaming environment. The implemented GA, refined through thorough grid search, provides a versatile framework for enhancing gameplay strategies and improving resource management in games like *Hollow Knight* thus, highlighting the synergy between computational intelligence and game strategy.

## References

* \[1\] Vanneschi, L., & Silva, S. (2023). Lectures on Intelligent Systems.
* \[2\] Miller B. L., Goldberg D. E. Genetic Algorithms, Tournament Selection and the Effects of Noise.
* \[3\] Pandey, H. M. (2016). Performance Evaluation of Selection Methods of Genetic Algorithm and Network Security Concerns.
* \[4\] Vanneschi L. (2024). Genetic Algorithms. NOVA IMS, Universidade Nova de Lisboa.
* \[5\] Pandey, H. M., Deepti Mehrotra, Anupriya Shukla. (2015). Comparative Review of Selection Techniques in Genetic Algorithm.
* \[6\] Hussain, A., Muhammad, Y. S., Sajid, M., Hussain, I., Shoukry, A. M., & Gani, S. (2017). Genetic Algorithm for Traveling Salesman Problem with Modified Cycle Crossover Operator.
* \[7\] Nitasha Soni, Dr Tapas Kumar. (2014). Study of Various Mutation Operators in Genetic Algorithms.
