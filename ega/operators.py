import random

def selection(np,fit):

    """Returns a list of indices of selected parents.

    This function takes the population size 'np' and the fitness of each individual of
    the population 'fit' and returns a list of indices of selected parents.
    """
    parents = []
    for i in range(np):
        ind1 = random.randint(0,np-1)
        ind2 = random.randint(0,np-1)
        if fit[ind1] < fit[ind2]:
            parents.append(ind1)
        else:
            parents.append(ind2)
    return parents

def onecrossover(parent1,parent2):

    """Returns two lists corresponding with the produced sons after the crossover
    operation.

    This function takes two chromosomes (parents) and performs the one point crossover
    operation and returns two chromosomes (sons).
    """
    n = len(parent1)
    cut = random.randint(0,n-1)
    son1 = parent1[0:cut]
    son11 = parent2[cut:n]
    son1.extend(son11)
    son2 = parent2[0:cut]
    son22 = parent1[cut:n]
    son2.extend(son22)
    return son1, son2

def parentscrossover(pc, population, parents):

    """Returns a list of sons after the crossover operation over the entire set
    of individuals in the populations.

    This function takes the crossover probability 'pc' in [0,1], the population
    of the chromosomes and a list of indices that contains the selected parents
    and returns a population of sons produced by the crossover operation.
    """
    np = len(population)
    sons = []
    for i in range(0,np,2):
        r = random.random()
        parent1 = population[parents[i]]
        parent2 = population[parents[i+1]]
        if r < pc:
            son1,son2 = onecrossover(parent1,parent2)
        else:
            son1,son2 = parent1,parent2
        sons.append(son1)
        sons.append(son2)
    return sons

def mutante(pm,son):

    """Returns a mutated son.

    This function takes the mutation probability 'pm' in [0,1], and a son of two parents
    and returns a mutated son by performing a bit flip mutation.
    """
    n = len(son)
    for i in range(n):
        r = random.random()
        if r < pm:
            if son[i] == 0:
                son[i] = 1
            else:
                son[i] = 0
    return son 

def xsonsmutantes(pm,sons):

    """Returns a list of mutated sons.

    This function takes the mutation probability 'pm' in [0,1] and a population of sons
    and returns a list of mutated sons.
    """
    xsons = []
    np = len(sons)
    for i in range(np):
        xson = mutante(pm,sons[i])
        xsons.append(xson)
    return xsons