import numpy as np
import matplotlib.pyplot as plt
import time
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

 # Distance calculator
def dist0(r1,r2, n):                            
    dist0 = np.sqrt((r1.x[n]-r2.x[n])**2 + (r1.y[n]-r2.y[n])**2 + (r1.z[n]-r2.z[n]) **2)
    return dist0

 #x acceleration of r1 due to r2, at the nth time
def funkyfuncx(r1, r2, n, distance):
    xdoubledot = -(6.6738*10**-11  * r2.mass /distance**3) * ((r1.x[n]-r2.x[n]))
    return xdoubledot
    
 # same for y
def funkyfuncy(r1, r2, n, distance):
    ydoubledot = -(6.6738*10**-11  * r2.mass /distance**3) * ((r1.y[n]-r2.y[n]))
    return ydoubledot
    
 # and for z
def funkyfuncz(r1, r2, n, distance):
    zdoubledot = -(6.6738*10**-11  * r2.mass /distance**3)* ((r1.z[n]-r2.z[n]))
    return zdoubledot
    
 # gets n+1th x position due to its xvelocity and x TOTAL acceleration
def nextx(r1, n,distance, slices):
    nextx = r1.x[n] + slices * r1.xv[n] + 0.5* slices**2 * r1.xa[n]
    return nextx
    
 #same for y
def nexty(r1, n,  distance, slices):
    nexty = r1.y[n] + slices * r1.yv[n] + 0.5* slices**2 * r1.ya[n]
    return nexty
    
 # and for z    
def nextz(r1, n, distance, slices):
    nextz = r1.z[n] + slices * r1.zv[n] +0.5* slices**2 * r1.za[n]
    return nextz
#conversion factor for AU
auconvert = 1.496*10**11
daystoseconds = 24*3600






 ### CELESTIAL BODIES - [mass, xpos, ypos, zpos, xvel, yvel, zvel, xaccel, yaccel, zaccel] kg, m, m, m, m/s, m/s, m/s, m/s^2...
 
class Celestial:
    def __init__(self, mass, xpos, ypos, zpos,xvel, yvel, zvel, size):
        self.mass = mass
        self.x = [xpos]
        self.y = [ypos]
        self.z = [zpos]
        self.xv = [xvel]
        self.yv = [yvel]
        self.zv = [zvel]
        self.size = size
        self.xa = [0]
        self.ya = [0]
        self.za = [0]
        
        
# intial solar system values
smass = 1.989*(10**30)
emass = 5.9724*(10**24)
ex0 = 147.09*(10**9)
eyvel0 = 30.29*10**3
jmass = 1.898*10**27
marsmass = 6.39*10**23

#initial celestial bodies
sun = Celestial(smass,2.15*10**-3,5.81*10**-3,-1.29*10**-4,-5.34*10**-6,5.42*10**-6,1.27*10**-7,1.5)
earth = Celestial(emass, 7.89*10**-1, 6.10*10**-1, -1.56*10**-4, -1.08*10**-2, 1.36*10**-2, 1.70*10**-7, 0.1)
jupiter = Celestial(jmass, -4.53, -3.00, 1.14*10**-1,4.08*10**-3, -5.93*10**-3, -6.67*10**-5, .5 )       
mars = Celestial(marsmass, -1.61, 4.02*10**-1, 4.78*10**-2,-2.82*10**-3,-1.24*10**-2,-1.91*10**-4,0.1)

#list of all bodies to have them interact with each other but not themselves
bodies = [sun, earth, mars, jupiter]

#convert JPL horizons data from au/day to m/s
for abody in bodies:
	abody.x[0] = abody.x[0] * auconvert
	abody.y[0] = abody.y[0] *auconvert
	abody.z[0] = abody.z[0] *auconvert
	abody.xv[0] = abody.xv[0] *auconvert / daystoseconds
	abody.yv[0] = abody.yv[0] * auconvert / daystoseconds
	abody.zv[0] = abody.zv[0] *auconvert / daystoseconds
	

time0 = 0
tmax = 3600 * 8760 *10
slices = 36000
timer=time0
ncounter = 0


start_time = time.time()

for abody in bodies:
    #makes it so that a given body will interact with all OTHER bodies but not itself
    bodies2 = bodies.copy()
    bodies2.remove(abody)
        
    #initialize acceleration values, to be summed up
    
    xaccel1 = 0
    
    yaccel1 = 0
    
    zaccel1 = 0
        
    for bbody in bodies2:
        distance = dist0(abody, bbody, ncounter)
        xaccel1 += funkyfuncx(abody,bbody, ncounter, distance)
        yaccel1 += funkyfuncy(abody,bbody, ncounter,distance)
        zaccel1 += funkyfuncz(abody,bbody, ncounter,distance)
        
    #record summed up acceleration values
    abody.xa[0] = xaccel1
    abody.ya[0] = yaccel1
    abody.za[0] = zaccel1
        
while timer < tmax:
    for abody in bodies:
    

        
        #xaccel1 = abody.xa[ncounter]
        #yaccel1 = abody.ya[ncounter]
        #zaccel1 = abody.za[ncounter]

        #for bbody in bodies2:
        #    distance = dist0(abody, bbody, ncounter)
            #everyone gets their n+1 positions
        abody.x.append(nextx(abody,ncounter, distance, slices))
        abody.y.append(nexty(abody,ncounter, distance, slices))
        abody.z.append(nextz(abody,ncounter, distance, slices))

    for abody in bodies:
    
        bodies2 = bodies.copy()
        bodies2.remove(abody)
        
        xaccel1 = abody.xa[ncounter]
        yaccel1 = abody.ya[ncounter]
        zaccel1 = abody.za[ncounter]
        xaccel2 = 0
        yaccel2 = 0
        zaccel2 = 0

        for bbody in bodies2:
            distance = dist0(abody, bbody, ncounter)
            xaccel2 += funkyfuncx(abody,bbody, ncounter+1,distance)
            yaccel2 += funkyfuncy(abody,bbody, ncounter+1, distance)
            zaccel2 += funkyfuncz(abody,bbody, ncounter+1, distance)

        #everyone gets their n+1 TOTAL acceleration values  
        abody.xa.append(xaccel2)
        abody.ya.append(yaccel2)
        abody.za.append(zaccel2)
        
        abody.xv.append(abody.xv[ncounter] + slices*(xaccel1 + xaccel2)/2)
        abody.yv.append(abody.yv[ncounter] + slices*(yaccel1 + yaccel2)/2)
        abody.zv.append(abody.zv[ncounter] + slices*(zaccel1 + zaccel2)/2)
        
    timer += slices
    ncounter+=1
   


print("--- %s seconds ---" % (time.time() - start_time))  #benchmarking
#framesmax = tmax / 100
framesmax=87 
frames = 1


# beginning of writing the MEL file
with open('data.mel','w') as melfile:
    
    
    for abody in bodies:
        sizestr=str(abody.size)
        melfile.write("""sphere -p 0 0 0 -ax 0 1 0 -ssw 0 -esw 360 -r """)
        melfile.write(sizestr)
        melfile.write(""" -d 3 -ut 0 -tol 0.01 -s 8 -nsp 4 -ch 1;objectMoveCommand;\n""")
        
    #melfile.write("""sphere -p 0 0 0 -ax 0 1 0 -ssw 0 -esw 360 -r 0.1 -d 3 -ut 0 -tol 0.01 -s 8 -nsp 4 -ch 1;objectMoveCommand;\n""")
    #melfile.write("""setAttr "nurbsSphere1.translateX" """)
    #melfile.write("""5""")
    #melfile.write(""";\n""")

    #melfile.write("""if( `getAttr -k "nurbsSphere1.tx"` ) setKeyframe "nurbsSphere1.tx";\n""")
    #melfile.write("""if( `getAttr -k "nurbsSphere1.ty"` ) setKeyframe "nurbsSphere1.ty";
#if( `getAttr -k "nurbsSphere1.tz"` ) setKeyframe "nurbsSphere1.tz";
#if( `getAttr -k "nurbsSphere1.rx"` ) setKeyframe "nurbsSphere1.rx";
#if( `getAttr -k "nurbsSphere1.ry"` ) setKeyframe "nurbsSphere1.ry";
#if( `getAttr -k "nurbsSphere1.rz"` ) setKeyframe "nurbsSphere1.rz";
#if( `getAttr -k "nurbsSphere1.sx"` ) setKeyframe "nurbsSphere1.sx";
#if( `getAttr -k "nurbsSphere1.sy"` ) setKeyframe "nurbsSphere1.sy";
#if( `getAttr -k "nurbsSphere1.sz"` ) setKeyframe "nurbsSphere1.sz";
#if( `getAttr -k "nurbsSphere1.v"` ) setKeyframe "nurbsSphere1.v";\n""")

    while frames < framesmax:
        #convert to string
        framesstr = str(frames)
        nurbscounter=1
        melfile.write("""currentTime """)
        melfile.write(framesstr)
        melfile.write(""";\n""")
        for abody in bodies:
            xstr = str((abody.x[frames*100])/auconvert *3)
            ystr = str((abody.y[frames*100])/auconvert *3)
            nstr = str(nurbscounter)

            melfile.write("""setAttr "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".translateX" """)
            melfile.write(xstr)
            melfile.write(""";\n""")
            melfile.write("""if( `getAttr -k "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".tx"`||`getAttr -channelBox "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".tx"` )setKeyframe "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".tx";\n""")
            melfile.write("""setAttr "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".translateY" """)
            melfile.write(ystr)
            melfile.write(""";\n""")
            melfile.write("""if( `getAttr -k "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".ty"` ) setKeyframe "nurbsSphere""")
            melfile.write(nstr)
            melfile.write(""".ty";\n""")
            nurbscounter+=1
        frames += 1
