import stdio
import sys
import math

principal = float(sys.argv[1])
interest = float(sys.argv[2])
years = float(sys.argv[3])

output = principal*math.e**(interest*years)
stdio.writeln(output)