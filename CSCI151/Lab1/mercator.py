import math
import stdio
import sys

longMapCenterDegrees = float(sys.argv[1])
latitudeDegrees = float(sys.argv[2])
longitudeDegrees = float(sys.argv[3])

longMapCenter = math.radians(longMapCenterDegrees)
latitude = math.radians(latitudeDegrees)
longitude = math.radians(longitudeDegrees)

x = longitude - longMapCenter
y = 0.5*math.log((1+math.sin(latitude))/(1-math.sin(latitude)),math.e)

stdio.writeln(x)
stdio.writeln(y)