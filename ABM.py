## import packages
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import csv
import random as rn
import matplotlib.pyplot
import agentframework as af
import dog
import matplotlib.animation

## random seed
rn.seed(20)
## Number of agents variable:
num_of_agents = 18
num_of_sheepdogs = 1
## Number of iterations variable
num_of_iterations = 500
neighbourhood = 15
## Possible speed variable
s = 3
## create empty envirnment and elevation lists
environment = []
elevation = []
## animation figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True


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
## create empty sheep dog list
sheep_dog = []


## add i of agent class to agents list
for i in range(num_of_agents):
    agents.append(af.Agent(i, environment, agents, elevation, sheep_dog))
## add 1 sheep dog
for i in range(num_of_sheepdogs):
    sheep_dog.append(dog.Dog(i, agents, elevation))
"""
## this as a test to see if hunt moves the dog towards the sheep
for i in range(num_of_iterations):
    matplotlib.pyplot.xlim(0, 249)
    matplotlib.pyplot.ylim(0, 249)
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
    print(sheep_dog[0])
    sheep_dog[0].hunt(agents[0], 5)
    agents[0].move(10, s)
    matplotlib.pyplot.scatter(agents[0].x,agents[0].y, c = 'white', s=agents[i].store * 0.5)
    matplotlib.pyplot.scatter(sheep_dog[0].x,sheep_dog[0].y, c = 'black', s=20)
matplotlib.pyplot.show()
"""

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.draw() 

### create GUI window
root = tkinter.Tk() # main window
w = tkinter.Canvas(root, width=200, height=200)
w.pack() # Layout
w.create_rectangle(0, 0, 200, 200, fill="blue")
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
### Create GUI menu
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


 
## Randomly move each agent, make them eat and plot the new environment 
def update(frame_number):
    
    fig.clear()   
    global carry_on
    rn.shuffle(agents)
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
    #for i in range(num_of_iterations):
    a = sheep_dog[0].find_closest() # Sheep dog determines closest sheep
    sheep_dog[0].hunt(agents[a], s*0.8) # Sheep dog chases closest sheep
    
    for j in range(num_of_agents):
        agents[j].move(neighbourhood, sheep_dog[0], s)
        #agents[j].eat()
        agents[j].share_w_neighbours(neighbourhood)
        #agents[j].check_distance()
        #print(agents[j])
    
    if rn.random() < 0.01:
     carry_on = False
     #print("stopping condition")
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.5)
        matplotlib.pyplot.scatter(agents[a].x,agents[a].y, c = 'red', s=agents[i].store * 0.5)  # Chased sheep is colored red
    matplotlib.pyplot.scatter(sheep_dog[0].x,sheep_dog[0].y, c = 'black', s=20)

## create model animation stopping conditions
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
   
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#matplotlib.pyplot.show()
tkinter.mainloop()    
     
#print(agents)
