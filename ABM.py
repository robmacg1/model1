## import packages
import csv
import random as rn
import matplotlib.pyplot
import agentframework as af
## Create distance function


rn.seed(19)

def distance_between(a, b):
    """
    This is a function that calculates the distance betweeen two pairs of coordinates.

    Parameters
    ----------
    a : List with at least 2 items, y coordinate and x coordinate
        This list refers to the location of the first agent
    b : List with at least 2 items, y coordinate and x coordinate
        This list refers to the location of the second agent

    Returns
    -------
    Float
        Euclidean distance between the 2 pairs of coordinates

    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5


## Number of agents variable:
num_of_agents = 15
## Number of iterations variable
num_of_iterations = 100
## Possible speed variable
s = 3
## create empty envirnment list
environment = []
store = 5


## Read in env data
with open('env.csv', newline="") as e:
    reader = csv.reader(e, delimiter = ",", quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
    #matplotlib.pyplot.imshow(environment)
    #matplotlib.pyplot.show()
e.close()
## copy environment list to keep a list of elevations
elevation = environment.copy()

   
## create empty agents list
agents = []

## add i of agent class to agents list
for i in range(num_of_agents):
    agents.append(af.Agent(i, environment, store, elevation))

## Randomly move each agent, make them eat and plot the new environment 
for i in range(num_of_iterations):
   for j in range(num_of_agents):
       agents[j].move(s)
       agents[j].eat()
       print(agents[j])
   matplotlib.pyplot.xlim(0, 249)
   matplotlib.pyplot.ylim(0, 249)
   matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.2)
matplotlib.pyplot.show()

   
       
#for i in range(num_of_agents):
#   print(agents[i])

## Create empty list for distances
distances = []
"""
for j in range(0,num_of_agents,1):
    for k in range(j+1,num_of_agents,1):
            d = distance_between(agents[j], agents[k])
            distances.append(d)
            mind = min(distances)
            
"""


