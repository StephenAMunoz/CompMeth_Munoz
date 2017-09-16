import matplotlib.pyplot as plt
import numpy as np

# Mandelbrot eqn.  z' = z^2 + c
# c complex constant, TO BE GENERATED IN NxN MATRIX
# c = complex(x,y)
# c = x + yj
import time
start_time=time.time()

def iters():   #iterations input with idiotproofing
	iterations1 = float(input("Please enter the number of iterations per value of c (positive integer values only): "))   #troll this!
	if (iterations1 <1) or ((iterations1/np.floor(iterations1) - 1) > 0.0001):   #trying to catch them entering negative numbers OR NONintegers, while accounting for the fact that floats are not perfect!
		print("Read the instructions!")
		iters()
	else:
		iterations2 = int(np.rint(iterations1))
		return iterations2

def matrixlen():  # N input with idiotproofing
	matlen = float(input("Please enter the number of slices per dimension for the grid (positive integer values only): "))   #troll this!
	if (matlen <1) or ((matlen/np.floor(matlen) - 1) > 0.0001):   #trying to catch them entering negative numbers OR NONintegers, while accounting for the fact that floats are not perfect!
		print("Read the instructions!")
		matrixlen()
	else:
		matlen2 = int(np.rint(matlen))
		return matlen2



iterations = 100#iters()
gridlength = 1000#matrixlen()

DaBrot = np.zeros([gridlength, gridlength], complex) # holds z's
x1 = np.linspace(-2,2, gridlength)
y1 = np.linspace(-2,2, gridlength)

complexconst = np.empty([gridlength, gridlength], complex) # holds the COMPLEX CONSTANTS
gvals = np.zeros((gridlength, gridlength), int) # holds the final number of iterations to hit 2 for each value
DaBrotiters = np.zeros([gridlength,gridlength],int) # will make a matrix of 1s or 0s based on if the z abs val exceeded 2


for x, xv in enumerate(x1):
    for y, yv in enumerate(y1):
        complexconst[x,y] = xv+ yv*1j #initializes matrix of complex constants
itrs=0

while itrs < iterations:
	itrs += 1
	DaBrot = DaBrot * DaBrot + complexconst   #steps the whole matrix of z values forward
	DaBrotabs= np.absolute(DaBrot)   # creates a matrix of abs(z)

	DaBrotiters=(np.greater((DaBrotabs-2),0)*1)  #Creates a matrix which is 0 where abs(z) <2, or 1 where abs(z) >2


	gvals = gvals+DaBrotiters*itrs  #if abs(z) exceeded 2, this matrix holds the iteration that it occured at
	DaBrot = DaBrot*(1-DaBrotiters)  # Kills the positions that exceeded 2 so it will never move again
	complexconst = complexconst *(1-DaBrotiters) # kills the positions that exceeded 2 so it will never move again

gvals[gvals<0.5] = itrs  # all positions that never exceeded 2 are set to max iterations value
gvals = -np.log(gvals)  # make it prettier
print("--- %s seconds ---" % (time.time() - start_time))  #benchmarking
plt.imshow(gvals.T, cmap="seismic", origin = "lower", extent=[-2,2,-2,2])
plt.show()

# Faster than looping by a factor of 5
