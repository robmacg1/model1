## import packages
import csv
import random as rn
import matplotlib.pyplot
import agentframework as af
import matplotlib.animation

## random seed
rn.seed(20)
## Number of agents variable:
num_of_agents = 5
## Number of iterations variable
num_of_iterations = 50
neighbourhood = 20
## Possible speed variable
s = 3
## create empty envirnment and elevation lists
environment = []
elevation = []
## set initial agent store
store = 5
## animation figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


## Read in env data
with open('env.csv', newline="") as e:
    reader = csv.reader(e, delimiter = ",", quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        #elevation.append(rowlist)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.show()
e.close()

## copy environment list to keep a list of elevations
ncol = len(environment[0])
for i in range(len(environment)):
    rowlist = []
    for j in range(ncol):
        rowlist.append(j)
    elevation.append(rowlist)
    
## create empty agents list
agents = []

## add i of agent class to agents list
for i in range(num_of_agents):
    agents.append(af.Agent(i, environment, agents, store, elevation))

for i in agents:
    type(agents[i])


carry_on = True	
## Randomly move each agent, make them eat and plot the new environment 
def update(frame_number):
    
    fig.clear()   
    global carry_on
    rn.shuffle(agents)
    #for i in range(num_of_iterations):
    for j in range(num_of_agents):
        agents[j].move(s)
        agents[j].eat()
        agents[j].share_w_neighbours(neighbourhood)
        #agents[j].check_distance()
        print(agents[j])
    matplotlib.pyplot.xlim(0, 249)
    matplotlib.pyplot.ylim(0, 249)
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
    if rn.random() < 0.01:
     carry_on = False
     print("stopping condition")
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.5)
    matplotlib.pyplot.show()

## create model animation stopping conditions
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
   
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)

matplotlib.pyplot.show()
   
     
print(agents)
