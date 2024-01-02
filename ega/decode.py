def transformer(chromosome_section):
    
    """Returns the integer that corresconds with a binary section of the chromosome.

    This function takes a list with binary integer values in {0,1} that corresponds
    with a variable of the optimization problem and returns the corresponding integer
    in the decimal numerical system.
    """
    bucket = 0
    for i,j in enumerate(chromosome_section):
        bucket = bucket + j*(2**i)
    integer = bucket
    return integer

def getlimits(nbits):

    """Returns the indices of the extreme values of each chromosome section.

    This function takes a list with 'd' integers that indicates the number of bits
    per variable of the optimization problem and returns two lists with the start
    and stop values of each chromosome section.
    """
    superstart = []
    superstop = []
    start = 0
    stop = nbits[0] - 1
    superstart.append(start)
    superstop.append(stop)
    for i in range(len(nbits)-1):
        start = stop + 1
        stop = stop + nbits[i+1]
        superstart.append(start)
        superstop.append(stop)
    return superstart,superstop

def decode(chromosome,nbits,parameters):

    """Returns a list with the decoded continuous values of each variable of the problem.

    This function takes the chromosome (binary list), the number of bits per variable (nbits)
    and a dictionary of some parameters of the problem and returns the decoded continuous values
    of the problem.
    """
    x = []
    superstart, superstop = getlimits(nbits)
    for i in range(len(nbits)):
        schromosome = chromosome[superstart[i]:superstop[i]+1]
        integer = transformer(schromosome)
        linf = parameters['linf'][i]
        lsup = parameters['lsup'][i]
        Val = linf + (integer/(2**(nbits[i])-1))*(lsup-linf)
        x.append(Val)
    return x