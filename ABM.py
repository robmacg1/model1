# =============================================================================
# Agent Based Model python script version 1.0
# Created by Rory MacGregor
# =============================================================================

# =============================================================================
# Import packages
# =============================================================================
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import csv
import random as rn
import matplotlib.pyplot
import agentframework as af
import matplotlib.animation
import requests
import bs4

# =============================================================================
# DEFINE FUNCTIONS
# =============================================================================
def run():
    """
    funtion to run animation.

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=stop_condition(num_of_agents), repeat=False)
    #animation.save('animation.gif', writer='pillow')
    canvas.draw() 
    
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

def no_alive(agents):
    """
    Goes through a list of agents and counts how many have died
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
        if agents[i].living == 0:
            a += 1
    return a
            
## create model animation stopping conditions
def stop_condition(num_of_agents, b = [0]):
    """
    Function for the frames argument in run fucntion that keeps the framescount increasing until the
    stop conditions are met. In this case that the number of eaten agents is half of the number
    of agents generated when the model is run.

    Parameters
    ----------
    b : number, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    Number
        outputs 1 more than the last call and waits for the next call until conditions are met to print that
        they have been.

    """
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (no_eaten(agents) != (num_of_agents*0.5)) or (no_alive(agents) < (0.5 * num_of_agents)):
        yield a			# Returns control and waits next call.
        a = a + 1
        #print(a)
    
    else:
        print("Stopping condition")
        a = open("model_output.txt", "w")
        a.write("Model Iterations: " + str(num_of_iterations) + " ")
        for i in agents:
            a.write("|" + str(i) + " ")
        a.close()
        
## Randomly move each agent depending on elevation, make them eat, share and plot the new environment.  
def update(frame_number):
    """
    Function to make the agents interact with their environment, each other each frame.

    Parameters
    ----------
    frame_number : number
        

    Returns
    -------
    None.

    """
    fig.clear()   
    global num_of_iterations
    global carry_on
    #rn.shuffle(agents) ## randomizing agent list broke the sheepdog's find_closest function
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 255)
    a = sheep_dog[0].find_closest() # dog determines closest sheep
    sheep_dog[0].hunt(agents[a], s * dog_speed) # dog chases closest sheep 
    for j in range(num_of_agents):
        agents[j].move(neighbourhood, sheep_dog[0], wariness, s)
        agents[j].share_w_neighbours(neighbourhood)
        agents[j].survive(sheep_dog[0], lifespan)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'white', s=agents[i].store * 0.5)
        #matplotlib.pyplot.scatter(agents[a].x,agents[a].y, c = 'red', s=agents[i].store * 0.5)  # Chased sheep is colored red
    matplotlib.pyplot.scatter(sheep_dog[0].x,sheep_dog[0].y, c = 'black', s=20)
    #for i in agents:
        #print(i)
    
    #print(no_eaten(agents)) # This tested the no_eaten function
    num_of_iterations += 1

# =============================================================================
# MODIFIABLE MODEL VARIABLES
# =============================================================================
## random seed
rn.seed(35)
## Number of agents variable (Can't be more than 100 now web scraping implemented):
num_of_agents = 75
# Number of sheep dogs variable (CAN ONLY BE 1):
num_of_sheepdogs = 1
## Number of iterations variable (left over from before stopping condition implemented)
num_of_iterations = 0
## Distance sheep share with each other and flock together
neighbourhood = 5
## Distance sheep run from the sheepdog
wariness = 25
## Sheep Lifespan in bowel movements
lifespan = 4
## Possible speed variable
s = 3
## Dog speed factor
dog_speed = 0.9
## create empty environment and elevation lists
environment = []
elevation = []
## animation figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True

# =============================================================================
# CREATE GUI 
# =============================================================================
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

# =============================================================================
# Web scrape page to get initial coordinates for agents
# =============================================================================
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 

# =============================================================================
# Read in data for environment variables
# =============================================================================
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

## copy environment list to keep a list of elevations that won't change when the sheep eat
ncol = len(environment[0])
for i in range(len(environment)):
    rowlist = []
    for j in range(ncol):
        rowlist.append(j)
    elevation.append(rowlist)
    
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
# =============================================================================
# CREATE AGENTS    
# =============================================================================
## create empty agents list
agents = []
## create empty sheep dog list
sheep_dog = []

## add i of agent class to agents list
for i in range(num_of_agents):
    if (int(td_ys[i].text) == None):
        y = rn.randint(125,175)
    else:
        y = int(td_ys[i].text)
        
    if (int(td_xs[i].text) == None):
        x = rn.randint(125,175)
    else:
        x = int(td_xs[i].text)
    agents.append(af.Agent(i, environment, agents, elevation, sheep_dog, y, x))
## add 1 sheep dog
for i in range(num_of_sheepdogs):
    sheep_dog.append(af.Dog(i, agents, elevation))
    
tkinter.mainloop()    
     
# =============================================================================
# END OF SCRIPT
# =============================================================================
