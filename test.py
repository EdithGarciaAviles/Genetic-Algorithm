# Libraries
from ega import setparams, genetic_algorithm, objective_functions
from ega.decode import decode

# Mccormick functions parameters
parameters = {'linf':[-1.5,-3],'lsup':[4,4],'precision':6}

# Objective function
objfunction = objective_functions.mccormick

pc = 0.9   # Crossover probability (pc)
pm = -1    # Mutation probability (pm)
np = 100   # Population size
g = 1000   # Generations numbers
parameters = setparams.setparams(objfunction, parameters, np, g, pc, pm) # Setup parameters
bestchromosome, bestfit = genetic_algorithm.ga(parameters) # Results

nbits = parameters['nbits']                       # Number of bits per variable
xbest = decode(bestchromosome, nbits, parameters) # Decoded solutions

# Print results
print(f'The best solution (chromosome): \n {bestchromosome}')
print(f'The best solution (decoded): \n {xbest}')
print(f'Fitness of the best solution (bestfit): \n {bestfit}')
