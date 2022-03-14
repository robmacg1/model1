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
rn.seed(30)
## Number of agents variable:
num_of_agents = 150
num_of_sheepdogs = 1
## Number of iterations variable
num_of_iterations = 0
## Distance sheep share with each other and flock together
neighbourhood = 20
## Distance sheep run from the wolf
wariness = 150
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
    #matplotlib.pyplot.show()
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
    """
    funtion to run animation.

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=stop_condition, repeat=False)
    #animation.save('animation.gif', writer='pillow')
    canvas.draw() 

### create GUI window
root = tkinter.Tk() # main window
w = tkinter.Canvas(root, width=200, height=200)
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
### Create GUI menu
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

## Randomly move each agent depending on elevation, make them eat, share and plot the new environment.  
def update(frame_number):
    fig.clear()   
    global num_of_iterations
    global carry_on
    #rn.shuffle(agents) ## randomizing agent list broke the sheepdog's find_closest function
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
    a = sheep_dog[0].find_closest() # dog determines closest sheep
    sheep_dog[0].hunt(agents[a], s * 1.8) # dog chases closest sheep
    for j in range(num_of_agents):
        agents[j].move(neighbourhood, sheep_dog[0], wariness, s)
        agents[j].share_w_neighbours(neighbourhood)
        agents[j].survive(sheep_dog[0])
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.5)
        matplotlib.pyplot.scatter(agents[a].x,agents[a].y, c = 'red', s=agents[i].store * 0.5)  # Chased sheep is colored red
    matplotlib.pyplot.scatter(sheep_dog[0].x,sheep_dog[0].y, c = 'black', s=20)
    #for i in agents:
        #print(i)
    
    #print(no_eaten(agents)) # This tested the no_eaten function
    num_of_iterations += 1
    

def no_eaten(agents):
    """
    Goes through a list of agents and counts how many have been eaten
    Parameters
    ----------
    agents : List
        A list of instances of the agent class.

    Returns
    -------
    a : Number
        a count of how many agents are currently eaten

    """
    a = 0
    for i in range(num_of_agents):
        if agents[i].eaten == True:
            a += 1
    return a
            

## create model animation stopping conditions
def stop_condition(b = [0]):
    """
    Function for the frames argument in run fucntion that keeps the framescount increasing until the
    stop conditions are met. In this case that the number of eaten agents is half of the number
    of agents generated when the model is run.

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    Number
        outputs 1 more than the last call and waits for the next call until conditions are met to print that
        they have been.

    """
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (no_eaten(agents) != (num_of_agents*0.5)):
        yield a			# Returns control and waits next call.
        a = a + 1
        #print(a)
    
    else:
        print("Stopping condition")
        a = open("model_output.txt", "w")
        a.write("Model Iterations: " + str(num_of_iterations))
        for i in agents:
            a.write("|" + str(i) + " ")
        a.close()
        
   
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#matplotlib.pyplot.show()
tkinter.mainloop()    
     
