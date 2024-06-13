# Date: Jun 12 2024
# Author: Kathryn Schneider
# Goals: Build a function which calculates the dV required to raise an orbit to 410,000 km 
            # Call from separate file 
            
from Homework_2_File1 import apoapsisEq

OGapoapsis=int(input("What is the original apoapsis?: "))

deltaV=apoapsisEq(OGapoapsis)
print('The '+'\u0394'+'V required to raise this object\'s orbit to 140,000km is: '+str(deltaV)+' m/s')