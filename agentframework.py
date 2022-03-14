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
        self.living = 1
        self.eaten = False
        
        
    def __str__(self):
        return ("id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + 
                ", store =" + str(self.store) + ", count =" + str(self.count) + ", Living =" + str(self.living))
    
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
        """
        Funtion that checks how close the nearest other agent is from self

        Returns
        -------
        Number
            Value for the distance of the closest other agent

        """
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
        
    def move(self, neighbourhood, dog, wariness = 50, s = 1):
        """
        Move function. Checks distance between self and dog, if dog is too close then self moves in the opposite direction from dog.
        Checks if elevation difference is to high to move in a random direction. Checks if other agents are within neighbourhood, if so
        then agent movement speed and chance to move is lowered.

        Parameters
        ----------
        neighbourhood : The distance agents check other agents are within
        s : Speed, optional
            DESCRIPTION. The default is 1.

        Returns
        -------
        None.

        """
        self.store -= 1
        if self.living > 0:
            if self.distance_between(dog) > wariness:
                min_d = self.check_distance() ## check for nearest sheep
                self.eat() ## eat before moving
                if min_d > neighbourhood: ## if nearest sheep is futher than neighbourhood then move freely
                    x = self.move_xory(self.x, s) #hypothetical new position
                    y = self.move_xory(self.y, s) #
                    dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])# difference in elevation of new and current position 
                    if dif < 5: # if difference in elevation is low then move is made
                        self.x = x
                        self.y = y
                        if self.store > s:
                            self.store = self.store - (s-1) # movement costs calories
                if min_d <= neighbourhood and rn.random() >0.6: ## if a sheep is nearby then less likely to move and will go slower
                   x = self.move_xory(self.x, 1) #hypothetical new position
                   y = self.move_xory(self.y, 1) #
                   dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])# difference in elevation of new and current position 
                   if dif < 3: # if difference in elevation is low then move is made
                       self.x = x
                       self.y = y
                       if self.store > s:
                           self.store = self.store - (s-1) # movement costs calories
                           
            else:
                x = self.move_away(self.x, dog.x, s) #hypothetical new position
                y = self.move_away(self.y, dog.y, s)
                dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])# difference in elevation of new and current position 
                if dif < 6: # if difference in elevation is low then move is made (higher than in grazing because they are being chased)
                    self.x = x
                    self.y = y
                #self.x = self.move_away(self.x, dog.x, s)
                #self.y = self.move_away(self.y, dog.y, s)
            
           
        
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 5 # half calories lost to life processes 
            '''
            self.environment[self.y-1][self.x-1] -=3
            self.environment[self.y][self.x-1] -=3
            self.environment[self.y-1][self.x] -=3
            self.environment[self.y+1][self.x+1] -=3
            self.environment[self.y+1][self.x] -=3
            self.environment[self.y][self.x+1] -=3
            self.environment[self.y-1][self.x+1] -=3
            self.environment[self.y+1][self.x-1] -=3
            '''
        else: # eat what is left of the grass
            a = self.environment[self.y][self.x]
            self.store + (a/2) # half calories lost to mastication
            #print(self.environment[self.y][self.x], "before")
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            #print(self.environment[self.y][self.x], "after") 
           
            
        #else:
        #    self.environment[self.y][self.x] +=10
            
        if self.store >150:
            self.environment[self.y][self.x] += 100 # some grass eaten is non-digestible
            self.store = 10
            self.count += 1 # no. of bowel movements

    def survive(self, dog):
        if self.distance_between(dog) < 8:
            self.store -= 20
        
        if self.store < 0:
            self.store = 0
            self.living = 0
            self.eaten = True
            self.x = 500
            self.y = 500
            
            