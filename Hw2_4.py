import numpy as np
# tprime = t0*(gamma) time dilation
# xprime = x0 / gamma length contration
# gamma = 1/(sqrt(1-v^2 / c^2)) lorentz factor
# ta time in earth rest frame (y) to be calculated
# tb time in spaceship rest frame (y) to be calculated (THIS is the proper time!!)
# xa earth-target distance IN THE EARTH'S REST FRAME (ly) - to be input (proper length)
# xb earth-target distance IN THE SPACESHIP'S REST FRAME (ly) - to be input
# v velocity (c) - to be input

xa = float(input("Please input the distance from the Earth to the target, in light years: "))
v = float(input("Please input the speed of the spaceship AS A FRACTION OF THE SPEED OF LIGHT (less than 1!): "))
gamma = 1/(np.sqrt(1-(v**2)))  # lorentz factor
x0 = xa # proper length
xb = x0 / gamma   # spaceship rest frame
tb = xb / v  # proper time
t0 = tb

ta = tb*gamma  # spaceship rest frame

print (gamma)
print ("{} {} {}".format("Elapsed time in Earth's rest frame is", ta, "years."))
print ("{} {} {}".format("Elapsed time in the spaceship's rest frame is", tb, "years."))
