## import packages
import csv
import random as rn
import matplotlib.pyplot
import agentframework as af
## Create distance function


rn.seed(19)




## Number of agents variable:
num_of_agents = 30
## Number of iterations variable
num_of_iterations = 100
neighbourhood = 20
## Possible speed variable
s = 4
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
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.show()
e.close()


## copy environment list to keep a list of elevations
#elevation = environment.copy()
#
#environment[0][0] = -1
#print(elevation[0][0])
# this was a test to see i fthe 2 rasters were independent
print(len(environment[0]))
ncol = len(environment[0])
elevation = []
for i in range(len(environment)):
    rowlist = []
    elevation.append(rowlist)
    for j in range(ncol):
        print(environment[i][j])
        elevation[i][j] = environment[i][j]

environment[0][0] = -1
print(elevation[0][0])
# this was a test to see i fthe 2 rasters were independent        
    
## create empty agents list
agents = []

## add i of agent class to agents list
for i in range(num_of_agents):
    agents.append(af.Agent(i, environment, agents, store, elevation))

## Randomly move each agent, make them eat and plot the new environment 
for i in range(num_of_iterations):
   for j in range(num_of_agents):
       agents[j].move(s)
       agents[j].eat()
       agents[j].share_w_neighbours(neighbourhood)
       print(agents[j])
   matplotlib.pyplot.xlim(0, 249)
   matplotlib.pyplot.ylim(0, 249)
   matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
   for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.2)
   matplotlib.pyplot.show()

   
       
#for i in range(num_of_agents):
#   print(agents[i])



"""
for j in range(0,num_of_agents,1):
    for k in range(j+1,num_of_agents,1):
            d = distance_between(agents[j], agents[k])
            distances.append(d)
            mind = min(distances)
            
"""


