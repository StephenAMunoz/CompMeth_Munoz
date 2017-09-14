import numpy as np
import matplotlib.pyplot as plt

# Logistic map -     x' = rx(1-x)
# rconst - constant r to be determined by user (at first, later will be an array); to be plotted on horizontal axis
# rarr - new array to hold all the r's
# xindvar - independent variable x.  starts at 1/2, goes through iterator a bunch of times.  to be plotted on vertical axis
# xarr - new array to hold all the x's
# iterations - number of times to iterate the logistic map equation, ask user how many times

def iters():
	iterations1 = float(input("Please enter the number of iterations per value of r (positive integer values only):"))   #troll this!
	if (iterations1 <1) or ((iterations1/np.floor(iterations1) - 1) > 0.0001):   #trying to catch them entering negative numbers OR NONintegers, while accounting for the fact that floats are not perfect!
		print("Read the instructions!")
		iters()
	else:
		iterations2 = int(np.rint(iterations1))
		return iterations2

iterations = iters()
#rconst = float(input("Please enter value of constant r (any float is cool, if you mess this up congratulations): "))
rarr=np.arange(1.0,4.0,0.01)  # creates array from 1 to 4 in steps of 0.01
xarr=np.zeros(rarr.size)
xarr=xarr+(1/2) # initializes array full of 1/2s, to go along with rarr
def logmap(r,x):  #logistic map - will be called in iteration loop. takes current value, produces next value
	xnext = r*x*(1-x)
	return xnext


#for rconst in rarr:  #going to add a value to the x array for EACH r in the r array
#	xindvar=1/2
i = 0
while i < iterations:  #iteration loop
	xarr=logmap(rarr,xarr)    #xindvar=logmap(rconst,xindvar)
	i+=1
#	xarr=np.append(xarr, xindvar)  #after iterating the desired amount of times, append it to the array.  need to reassign the array cause append just sticks it to a COPY, doesnt modify original.


#print("Final value: {:E}".format(xindvar))
plt.scatter(rarr, xarr)
plt.show()

#question answers:
#Fixed point would not change with iteration
#limit cycle would move up and back down through the same values as iteration changes
#chaos point moves up and down unpredictably as iteration changes
#edge of chaos looks like it is just a bit past r=3.5
