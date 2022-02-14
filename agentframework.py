import random as rn

## initial food in stomach variable
#store = 5

class Agent:
    def __init__(self, i, environment, store, elevation):
        self.id = i
        self.x = rn.randint(0,249)
        self.y = rn.randint(0,249)
        self.environment = environment
        self.store = store
        self.count = 0
        self.elevation = elevation
        
    def __str__(self):
        return "id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + ", store =" + str(self.store) + ", count =" + str(self.count)

   
             
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
            xory = (xory + rn.randint(1, s)) % 250
        
        else:
            xory = (xory - rn.randint(1, s)) % 250
        return xory
            
    def move(self, s = 1):
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
        x = self.move_xory(self.x, s)
        y = self.move_xory(self.y, s)
        dif = abs(self.elevation[self.y][self.x] - self.elevation[y][x])
        print(str(self.elevation[self.y][self.x]) + ", " + str(self.elevation[y][x]) + ", "  + str(dif))
        if dif < 20:
            self.x = x
            self.y = y
        if self.store > s:
            self.store = self.store - (s-1)
        
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 20 and rn.random() < 0.8:
            self.environment[self.y][self.x] -= 20
            """
            self.environment[self.y-1][self.x-1] -=3
            self.environment[self.y][self.x-1] -=3
            self.environment[self.y-1][self.x] -=3
            self.environment[self.y+1][self.x+1] -=3
            self.environment[self.y+1][self.x] -=3
            self.environment[self.y][self.x+1] -=3
            self.environment[self.y-1][self.x+1] -=3
            self.environment[self.y+1][self.x-1] -=3
            """
            self.store += 10 # half calories lost to life processes
        #else:
        #    self.environment[self.y][self.x] +=10
            
        if self.store >150:
            self.environment[self.y][self.x] += 100 # some data eaten is non-digestible
            self.store = 10
            self.count = self.count + 1
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
            