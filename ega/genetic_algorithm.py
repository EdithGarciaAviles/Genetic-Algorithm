import copy
import numpy as nup
from .genesis import people
from .objective_functions import evalpopulation
from .operators import selection, parentscrossover, xsonsmutantes 

def ga(parameters):

    """Returns the best chromosome and it fitness found by the genetic algorithm.

    This function takes a dictionary with a set of parameters to setup the genetic
    algorithm and returns the best chromosome and it fitness found by the genetic algorithm.
    """
    nbits = parameters['nbits']             # Number of bits per variable
    n = parameters['n']                     # Total size of the chromosome
    pm = parameters['pm']                   # Mutation probability
    pc = parameters['pc']                   # Crossover probability
    np = parameters['np']                   # Population size
    g = parameters['g']                     # Number of generations
    objfunction = parameters['objfunction'] # Objetive function of the optimization problem.

    # Initialize the first population randomly
    population = people(n,np) 

    # Evaluate the fitness of the population
    fit = evalpopulation(population,nbits,parameters,objfunction) 

    # Get the best individual of the current generation
    bestfit = min(fit)
    bestindex = nup.argmin(fit)
    bestchromosome = population[bestindex]

    # Execute generations of the genetic algorithm
    for i in range(g):

        # Binary tournament selection
        parents = copy.deepcopy(selection(np,fit))   
        # Two points crossover
        sons = copy.deepcopy(parentscrossover(pc, population, parents))
        # Bit flip mutation
        xsons = copy.deepcopy(xsonsmutantes(pm, sons))
        # Replace the old generation with the mutated sons
        population = copy.deepcopy(xsons) 
        # Evaluate the fitness of the new population (mutated sons)
        fit = evalpopulation(population,nbits,parameters,objfunction) # Evaluar la aptitud de los individuos.
        # Get a fitness of the best individual of the new generation
        bestfit_currentg = min(fit)
        # Elitism operator (preserve the best individual along all generations) 
        if bestfit_currentg < bestfit:
            bestfit = bestfit_currentg 
            bestindex = nup.argmin(fit)
            bestchromosome = population[bestindex]
    return bestchromosome, bestfit