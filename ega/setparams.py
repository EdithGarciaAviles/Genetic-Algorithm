import math

def getbits(parameters):

    """Returns a list that contains the number of bits required by each
    variable of the optimization problem.

    This function takes a dictionary of parameters that contains the lower an upper
    values and the precision of each variable and returns a list that contains the
    number of bits required by each variable of the optimization problem.
    """
    d = len(parameters['linf'])
    nbits = []
    for i in range(d):
        range_ = parameters['lsup'][i]-parameters['linf'][i]
        states_ = range_*(10**parameters['precision'])
        nbits_ = math.ceil(math.log2(states_))
        nbits.append(nbits_)
    return nbits    

def setparams(objfunction, parameters, np, g, pc, pm):

    """Returns a dictionary that contains all the required parameters to
    setup the genetic algorithm.

    This function takes the objective function to optimize, a dictionary of few
    parameters, the population size, number of generations, crossover probability
    and mutation probability and returns a dictionary that contains all the required
    parameters to setup the genetic algorithm.
    """
    # Get the number of bits for each dimension (according the range and required precision)
    nbits = getbits(parameters) 
    n = sum(nbits)                                 
    if pm == -1:
        pm = 1/n                                   # Mutation probability
    parameters['nbits'] = nbits                    # Number of bits per dimension      
    parameters['n'] = n                            # Chromosome length    
    parameters['pm'] = pm                          # Mutation probability
    parameters['pc'] = pc                          # Crossover probability
    parameters['np'] = np                          # Population size
    parameters['g'] = g                            # Number of generations
    parameters['objfunction'] = objfunction        # Objective function
    return parameters