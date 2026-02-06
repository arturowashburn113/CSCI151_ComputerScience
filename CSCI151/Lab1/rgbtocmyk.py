import stdio
import sys

rComp = int(sys.argv[1])
gComp = int(sys.argv[2])
bComp = int(sys.argv[3])

w = max(rComp/255, gComp/255, bComp/255)

if rComp == gComp == bComp == 0:
    cComp = 0.0
    mComp = 0.0
    yComp = 0.0
    kComp = 1.0
else:
    cComp = (w-(rComp/255))/w
    mComp = (w-(gComp/255))/w
    yComp = (w-(bComp/255))/w
    kComp = 1-w
stdio.writeln("cyan = " + str(cComp))
stdio.writeln("magenta = " + str(mComp))
stdio.writeln("yellow = " + str(yComp))
stdio.writeln("black = " + str(kComp))