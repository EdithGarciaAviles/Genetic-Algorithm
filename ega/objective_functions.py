import math
from .decode import decode

"""TEST OBJECTIVE FUNCTIONS"""

def mccormick(x1,x2):
    return math.sin(x1 + x2) + (x1 - x2)**2 -1.5*x1 + 2.5*x2 + 1
    
def bukin(x1,x2):
    return 100*math.sqrt(abs(x2-0.01*x1**2)) + 0.01*abs(x1 + 10)

def CrossInTrayFunction(x1,x2):
    return -0.0001*(abs(math.sin(x1)*math.sin(x2)*math.exp(abs(100 - (math.sqrt(x1**2 + x2**2)/(math.pi)))))+1)**0.1

def eggholder(x1,x2):
    return -(x2 + 47)*math.sin( math.sqrt(abs(x2 + (x1/2) + 47)))- x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))

def levy(x1,x2):
    return  math.sin(3*math.pi*x1)**2 + ((x1 - 1)**2)*((1 + math.sin(3*math.pi*x2)**2) + ((x2 - 1)**2)*(1 + (math.sin(2*math.pi*x2)**2)))

def SixHumpCamel(x1,x2):
    return ((4 - 2.1*(x1**2) + ((x1**4)/3))*(x1**2) + (x1*x2) + (-4 + 4*(x2**2))*(x2**2))

def easom(x1,x2):
    return (-(math.cos(x1))*(math.cos(x2))*math.exp(-((x1 - math.pi)**2) - ((x2 - math.pi)**2)))

def evalpopulation(population,nbits,parameters,objfunction):

    """Returns the fitness of each individual of the population.

    This function takes a list of chromosomes (population), a list of the number of bits
    per variable (nbits), a dictionary of parameters and the objective functions to optimize.
    """
    fit = []
    for i in population:
        x = decode(i,nbits,parameters)
        x1 = x[0]
        x2 = x[1]
        f = objfunction(x1,x2)
        fit.append(f)
    return fit