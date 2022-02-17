### Agent 1 
### Import random and create random xy coords for 100*100 grid
import random
y0 = random.randint(0,99) 
x0 = random.randint(0,99) 

random_number = random.random()
if random_number <0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1

random_number2 = random.random()
if random_number2 <0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1
###############
random_number = random.random()
if random_number <0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1

random_number2 = random.random()
if random_number2 <0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1
#################
random_number = random.random()
if random_number <0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1
   
random_number2 = random.random()
if random_number2 <0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1
###############
random_number = random.random()
if random_number <0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1
   
random_number2 = random.random()
if random_number2 <0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1
####################
random_number = random.random()
if random_number <0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1
   
random_number2 = random.random()
if random_number2 <0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1
############### AGENT 1
#### Create random xy coords 100*100 GRID
y1 = random.randint(0,99) 
x1 = random.randint(0,99) 
if random.random() > 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() > 0.5:
    x1 += 1
else:
    x1 -= 1
#######    
if random.random() > 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() > 0.5:
    x1 += 1
else:
    x1 -= 1   
 ##########   
if random.random() > 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() > 0.5:
    x1 += 1
else:
    x1 -= 1
##########    
if random.random() > 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() > 0.5:
    x1 += 1
else:
    x1 -= 1       

print(y1, x1, y0, x0)
ydif = y0 - y1
xdif = x0 - x1
distance = ((ydif * ydif) + (xdif * xdif)) ** 0.5
print(distance)