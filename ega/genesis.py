import random

def genesis(n):

    """Returns the chromosome (binary list) from a given number of 'n' bits.

    This function takes a number of bits and returns a randomly generated list
    of 'n' bits.
    """
    chromosome =[]
    for i in range(n):
        gene = random.randint(0,1)
        chromosome.append(gene)
    return chromosome

def people(n,np):

    """Returns a list of chromosomes from a given numbers of 'n' bits and 'np' individuals.

    This function takes the number of bits of the chromosomes and the population size and
    returns the initial population of the genetic algorithm.
    """
    population = []
    for i in range(np):
        chromosome = genesis(n)
        population.append(chromosome)
    return population 