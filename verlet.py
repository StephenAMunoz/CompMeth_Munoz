import numpy as np
import matplotlib.pyplot as plt

# d^2r/dt^2 = -GM rvec/ r^3
# G = 6.6738E-11, M =1.9891E30 kg
# starting r = 1.4710E11m
# starting vel = 3.0287E4 in some direction! set it to be x
#calculate orbit of earth with verlet method time step slices = 1hr
#plot the orbit for several complete revolutions
#set dtheta/dt = w
# dw/dt  = -g/l sintheta

#two first order equations
#combine them into vectors, r=(theta,w)
#f will be vector function that acts on them


def funkyfunc(r,t):
    grav = 6.6738*10**-11
    mass = 1.9891*10**30  #kg
    dist0 = 1.4710*10**11  #m
    vel0 = 3.0287*10**4 #m/s

    pos=r[0]
    omega=r[1]
    ftheta=omega
    fomega = -(grav/leng)*np.sin(theta)
    return np.array([ftheta,fomega],float)

#solve the two first order equations, use 4th order runge kutta
#pendulum with 10cm aarm
#calulate theta as a function of t, released from a standstill of theta = 179 at t=0
#graph theta as a function of t
"""
4th order Runge kutta
dx/dt = f(x,t)

k1 = hf(x,t)
k2 = hf(x+1/2k1, t+1/2h)
k3 = hf(x+1/2k2, t+1/2h)
k4 = hf(x+k3,t+h)
x(t+h) = x(t) + 1/6(k1+2k2+2k3+k4)

iterate as long as you want

"""

slices = 0.001
theta0 = 179 / 180 * np.pi
omega0 = 0
time0 = 0
time = time0
rvec = [theta0,omega0]
thetavec = [theta0]
timevec = [time0]
while time < 4:
    k1 = slices *(funkyfunc(rvec,time))
    k2 = slices *(funkyfunc(rvec + 0.5*k1,time+0.5*slices))
    k3 = slices *(funkyfunc(rvec+0.5*k2, time+0.5*slices))
    k4 = slices *(funkyfunc(rvec+k3,time+slices))
    rvec = rvec + (1/6)*(k1 + 2*k2 + 2*k3 +k4)
    thetavec.append(rvec[0])
    time = time+slices
    timevec.append(time)
plt.scatter(timevec,thetavec)
plt.show()
