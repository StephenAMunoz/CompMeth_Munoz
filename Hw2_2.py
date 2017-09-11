import numpy as np

# h=(GMT^2 / 4pi^2) ^1/3 - R (m) to be output
# G grav constant (meters3 kg-1 s-2)
# M mass of earth (kg)
# R radius of earth (m)
# T period (s) to be input

R = 6371*(10**3)
G = 6.67*(10**-11)
M = 5.97*(10**24)

T = float(input("Please enter the desired period of the satellite in minutes: "))
T *= 60 # converts to seconds

h = (((G*M*(T**2))/(4*np.pi*np.pi))**(1/3)) - R
print ("{} {}".format(h, "meters."))

# 1440 minutes (1 "day"): 35856 km

# 90 minutes: 279 km

# 45 minutes: -2182 km - to achieve this period, the satellite would need to be
# orbiting the center of the earth at a distance below the earth's surface (and
# all of the earths mass would need to be concentrated below that radius)

# 1435.8 minutes (1 sidereal day): 35774 km - sidereal day is length of time
# for the earth to rotate once relative to the "fixed" stars. 1440 minutes
# is approximate amount of time to rotate once RELATIVE TO THE SUN, which is
# constantly changing position in our sky at a non-negligible rate due to our
# revolution around it.
