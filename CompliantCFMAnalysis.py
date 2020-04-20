#Crank slider analysis
#Jackson Empey
#MECH 461


import numpy as np
import matplotlib.pyplot as plt
import math

l1 = 0.0575*0.922*1
l2 = 0.054*0.922*1
#dx = 0.015
#k1 = 50
#k2 = 35

dx = np.linspace(0,0.02)
f = np.zeros(2*len(dx))
adfx = np.zeros(len(f)-1)

testAngles = np.linspace(np.deg2rad(30),np.deg2rad(20.2)) #angles going into the model
testX = np.zeros(len(testAngles)*2)
testStiffnessRatio = np.linspace(0.25,5,10) #Stiffnesses for testing
#the overall constant force capability is asessed by the average derivative of the f(x)


theta1Prime = testAngles[0]




def theta2x(theta):
    return math.sin(theta)*l1-math.sin(t1Tot2(theta))*l2

def theta2xAlt(theta):
    return math.sin(theta)*l1+math.sin(t1Tot2(theta))*l2

def t1Tot2(theta1):
    return math.acos(math.cos(theta1)*(l1/l2))

def force(t1, t2, theta1p, theta2p, k1, k2):
    return k1*(t1-theta1p)*(-math.sin(t2)/(l1*math.sin(t1-t2))) + k2*(t2-theta2p) * ( (-math.sin(t1))  /( l2 * math.sin(t1 - t2)) )



#print(np.deg2rad(testAngles))
print(str(theta1Prime) + ", " + str(t1Tot2(theta1Prime)) )

testAnglesRev = np.flip(testAngles)
print(testAnglesRev)
#testAngles = np.concatenate(testAngles, testAnglesRev)

testAnglesFull = np.zeros(2*len(testAnglesRev))
testAnglesFull[0:len(testAngles)] = testAngles
testAnglesFull[len(testAngles) : len(testAnglesFull)] = testAnglesRev

## FIRST FIND X0
for i in range (0,len(testAngles)):
    testX[i] = theta2x(testAnglesFull[i])
    
for i in range (len(testAngles),len(testAngles)*2):
    testX[i] = theta2xAlt(testAnglesFull[i])

for i in range(0,len(testAngles)):
    theta1 = testAnglesFull[i]
    theta2 = t1Tot2(theta1)
    
    f[i] = force(theta1, theta2, theta1Prime, t1Tot2(theta1Prime), 1, 4)
    print(str(theta1*(180/(np.pi))) + " T1, " + str(theta2*(180/(np.pi))) + " T2, " + str(testX[i]) + " X, " + str(f[i]) + " N")

for i in range(len(testAnglesRev),2*len(testAngles)):
    theta1 = testAnglesFull[i]
    theta2 = -t1Tot2(theta1)
    
    f[i] = force(theta1, theta2, theta1Prime, t1Tot2(theta1Prime), 1, 4)
    print(str(theta1*(180/(np.pi))) + " T1, " + str(theta2*(180/(np.pi))) + " T2, " + str(testX[i]) + " X, " + str(f[i]) + " N")
    

plt.plot(testX, f)
plt.xlabel("Displacement (m)")
plt.ylabel("Force (N)")
axes = plt.axes()
axes.set_ylim([0, 150])
axes.set_xlim([0, 0.07])
plt.show()

print("========================")
for i in range(0,len(testX)):
    print(str(testX[i]) + "," + str(f[i]))

