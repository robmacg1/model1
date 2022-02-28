import random as rn

class Agent:
    def __init__(self, i, environment, agents, elevation, sheep_dog):
        self.id = i
        self.x = rn.randint(0,299)
        self.y = rn.randint(0,299)
        self.environment = environment
        self.store = 5
        self.count = 0
        self.elevation = elevation
        self.agents = agents
        self.sheep_dog = sheep_dog
        
        
        
    def __str__(self):
        return ("id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + 
                ", store =" + str(self.store) + ", count =" + str(self.count))
    
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
        
    def share_w_neighbours(self, neighbourhood):
        """
        funtion that shares the stores of 2 agents within a vicinity of each other evenly

        Parameters
        ----------
        neighbourhood : Number
            Value for vicinity agents will share with each other within

        Returns
        -------
        Non

        """
        for i in self.agents:
            distance = self.distance_between(i)
            if distance <= neighbourhood:
                sum = self.store + i.store
                avg = sum/2
                self.store = avg
                i.store = avg
    
    def check_distance(self):
        distances = []
        for i in self.agents:
            distances.append(self.distance_between(i))
        s = set(distances)
        return sorted(s)[1] # second lowest distance excludes self
        
    
    def move_away(self, xory, dog, s):
        dist = xory - dog
        if dist > 0:
            xory = (xory + s) % 299
        
        else:
            xory = (xory - s) % 299
        return xory

    def move_xory(self, xory, s):
        """
        Move coordinates

        Parameters
        ----------
        xory : number
            Either x or y coordinate
        s : number
            "speed" (max distance that a coordinate can move by)

        Returns
        -------
        xory : number
            The new coordinate number (either the same or larger or smaller)

        """
        if rn.random() <0.33:
            return xory
        if rn.random() <0.5:
            xory = (xory + rn.randint(1, s)) % 299
        
        else:
            xory = (xory - rn.randint(1, s)) % 299
        return xory
        
    def move(self, neighbourhood, dog, s = 1):
        """
        Move function

        Parameters
        ----------
        s : Speed, optional
            DESCRIPTION. The default is 1.

        Returns
        -------
        None.

        """
        if self.distance_between(dog) > 40:
            min_d = self.check_distance() ## check for nearest sheep
            self.eat() ## eat before moving
            if min_d > neighbourhood: ## if nearest sheep is futher than neighbourhood then move freely
                x = self.move_xory(self.x, s) #hypothetical new position
                y = self.move_xory(self.y, s) #
                dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])# difference in elevation of new and current position 
                #print(str(self.elevation[self.y][self.x]) + ", " + str(self.elevation[y][x]) + ", "  + str(dif))
                if dif < 5: # if difference in elevation is low then move is made
                    self.x = x
                    self.y = y
                    if self.store > s:
                        self.store = self.store - (s-1) # movement costs calories
            if min_d <= neighbourhood and rn.random() >0.6: ## if a sheep is nearby then less likely to move and go slower
               x = self.move_xory(self.x, 1) #hypothetical new position
               y = self.move_xory(self.y, 1) #
               dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])# difference in elevation of new and current position 
               #print(str(self.elevation[self.y][self.x]) + ", " + str(self.elevation[y][x]) + ", "  + str(dif))
               if dif < 5: # if difference in elevation is low then move is made
                   self.x = x
                   self.y = y
                   if self.store > s:
                       self.store = self.store - (s-1) # movement costs calories
                       
        else:
            self.x = self.move_away(self.x, dog.x, s)
            self.y = self.move_away(self.y, dog.y, s)
            
           
        
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 20 and rn.random() < 0.8:
            self.environment[self.y][self.x] -= 20
            self.store += 10 # half calories lost to life processes 
            self.environment[self.y-1][self.x-1] -=3
            self.environment[self.y][self.x-1] -=3
            self.environment[self.y-1][self.x] -=3
            self.environment[self.y+1][self.x+1] -=3
            self.environment[self.y+1][self.x] -=3
            self.environment[self.y][self.x+1] -=3
            self.environment[self.y-1][self.x+1] -=3
            self.environment[self.y+1][self.x-1] -=3

        else: # eat what is left of the grass
            a = self.environment[self.y][self.x]
            self.store + (a/2) # half calories lost to mastication
            a - a
            
           
            
        #else:
        #    self.environment[self.y][self.x] +=10
            
        if self.store >150:
            self.environment[self.y][self.x] += 100 # some data eaten is non-digestible
            self.store = 10
            self.count = self.count + 1 # no. of bowel movements
"""        
if ((self.environment[self.y][self.x] - self.environment[self.y][self.x - 1] > 4) or 
    (self.environment[self.y][self.x] - self.environment[self.y][self.x + 1] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y - 1][self.x - 1] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y - 1][self.x + 1] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y + 1][self.x - 1] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y + 1][self.x + 1] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y - 1][self.x] > 4) or
    (self.environment[self.y][self.x] - self.environment[self.y + 1][self.x] > 4)):
        
    
            
 """           
            