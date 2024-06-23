# Date: Jun 12 2024
# Author: Kathryn Schneider
# Goals: Build a function which calculates the dV required to raise an orbit to 410,000 km
            # Call from separate file
            # Hints:
                # Input: original apoapsis altitude (high point)
                # Output: delta v (in m/s)
                # Use the vis-visa equation for each orbit and subtract the two to get the velocity difference
                # To call a function from another file, place them in the same directory and use an Import statement
               
# Importing libraries
import math
   
# Defining dV apoapsis equation
def ApogeeRaise (OGapoapsis):
    # Defining mu in km^2/s^2
    u=398600
   
    # Defining intial r using input info
    r1=185+6378
   
    # Defining initial a using input info
    a1=(6563+OGapoapsis+6378)/2
   
    # Defining equation to find initial velocity
    v1=math.sqrt(u*((2/r1)-(1/a1)))
   
    # Converting v1 from km/s to m/s
    v1m=v1*1000
   
    ## Defining final r
    r2=185+6378
   
    # Defining final a
    a2=(6378+185+410000+6378)/2
   
    # Defining equation to find initial velocity
    v2=math.sqrt(u*((2/r2)-(1/a2)))
   
    # Converting v2 from km/s to m/s
    v2m=v2*1000
   
    # Change in v (delta v in m/s)
    deltaV=v2m-v1m
   
    return deltaV