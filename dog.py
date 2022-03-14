import random as rn
import pandas as pd
class Dog:
    def __init__(self, i, agents, elevation):
        self.id = i
        self.x = rn.randint(0, 299)
        self.y = rn.randint(0, 299)
        self.elevation = elevation
        self.agents = agents
    
    def __str__(self):
        return "id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y)
    
    def hunt(self, i, s = 1):
            self.x = self.move_xory(self.x, i.x, s)
            self.y = self.move_xory(self.y, i.y, s)
        
    def move_xory(self, xory, agent, s):
        dist = xory - agent
        #if rn.random() <0.33:
        #    return xory
        if dist > 0:
            xory = (xory - s) % 300
        
        else:
            xory = (xory + s) % 300
        return xory
    
    def distance_between(self, agent):
            """
            This is a function that calculates the distance betweeen two agents
        
            Parameters
            ----------
            a : an agent class object with x and y coordinates
            b : an agent class object with x and y coordinates
        
            Returns
            -------
            Float
                Euclidean distance between the 2 agents
        
            """
            return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
        
    def find_closest(self):
        distances = []
        for i in self.agents:
            if i.living > 0:
                distances.append([i.id, self.distance_between(i)])    
        #min_d = (min(j[1]) for j in distances) ## couldn't work out how to return the corresponding id for the min distance
        df = pd.DataFrame.from_records(distances, columns=['ID','Distance']) 
        min_d = int(df.loc[df['Distance'].idxmin()]['ID'])
        #print(df)
        #print(min_d)
        return min_d
        
