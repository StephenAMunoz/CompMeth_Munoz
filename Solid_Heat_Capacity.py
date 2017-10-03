import numpy as np
import gaussxw as gxw
import matplotlib.pyplot as plt
volume = 1000 * 10**-6
rho = 6.022*10**28
boltz =1.381*10**-23
debyet = 428

#temperature = input("Please input temperature in KELVIN (positive numbers!):")

def funkyfunc(x):
    fx = x**4 * np.exp(4) / (np.exp(x) - 1)**2
    return fx

cvals = np.array([])
tvals = np.array([])

for T in range(5,501):
    const = 9*volume*rho*boltz*(T/debyet)**3
    points,weights = gxw.gaussxwab(50, 0, debyet/T )
    cval = const * sum(weights*funkyfunc(points))
    cvals =np.append(cvals,cval)
    tvals = np.append(tvals,T)



plt.scatter(tvals, cvals)
plt.show()
