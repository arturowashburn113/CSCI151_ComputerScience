import random
import math
import stdio
random.seed(1)
randomU = random.random()

randomV = random.random()

gaussianNumber = math.sin(2*math.pi*randomV)*math.sqrt(-2*math.log(randomU,math.e))
stdio.writeln(gaussianNumber)