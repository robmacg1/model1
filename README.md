# Agent Based Model Submission
## Sheep on a hill by Rory MacGregor
File descriptions:
1. This readme: Info on how to run the model or modify it if desired
2. ABM.py: The model python script file - this is the file to run
3. agentframework.py: This python script contains the sheep and dog classes and all their associated functions
4. Env.csv: This is a grid of numbers that the model reads in and uses as the environment and elevation data
5. Animaion.gif: This is an animation of an old version of the model that it used to output.

To run the model ABM.py should be opened and run. Then when the GUI opens the model can be run from the drop down menu. The model will run and update visually until the stop condition is met at which point it will output a text file containing how many iterations it took to finish and information about each agent.
There are variables within ABM.py that can be modifed to change how the model will play out including: 
1. The random seed 
2. The number of sheep, 
3. How fast the sheep can possibly move, 
4. How close the sheep dog can get before the sheep run away, 
5. How far away another sheep has to be to be considered within the neighborhood of another sheep 
6. The lifespan of each sheep in bowel movements.
