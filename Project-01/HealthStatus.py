# import random
from random import randint
import math

level = 1
health = 100

# healthStatus = health - random.randint(10,40)
healthStatus = int(health - randint(10,40) / level)

print(healthStatus)

# few math functions
math.round()
math.ceil()
math.floor()