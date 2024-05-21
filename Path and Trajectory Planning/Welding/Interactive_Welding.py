import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH


# link lengths in mm
a1 = float(input("a1 = ")) # for testing,150mm
a2 = float(input("a2 = ")) # for testing,150mm
a3 = float(input("a3 = ")) # for testing,150mm
a4 = float(input("a4 = ")) # for testing,150mm

# link converted to meters
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)

# link limits converted to meters
lm1 = float(input("lm1 = ")) # 50mm
lm1 = mm_to_meter(lm1)
lm2 = float(input("lm2 = ")) # 50mm
lm2 = mm_to_meter(lm2)
lm3 = float(input("lm3 = ")) # 50mm
lm3 = mm_to_meter(lm3)


# Create Links
CARTESIAN = DHRobot([
    PrismaticDH(0,0,(270/180)*np.pi,a1,qlim=[0,0]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0,lm1]),
    PrismaticDH((270/180)*np.pi,0,(90/180)*np.pi,a3,qlim=[0,lm2]),
    PrismaticDH(0,0,0,a4,qlim=[0,lm3])
], name='CARTESIAN')

print('CARTESIAN')


# q paths

#degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi



# q paths
q0 = np.array([0,0,0,0])

q1 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                ])

q2 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(15)),
                mm_to_meter(float(30)),
                ])

q3 = np.array([0,mm_to_meter(float(0)),
                mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                ])

q4 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(0)),
                mm_to_meter(float(10)),
                ])
            
q6 = np.array([0,0,0,0])

q7 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                ])

q8 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(15)),
                mm_to_meter(float(30)),
                ])

q9 = np.array([0,mm_to_meter(float(0)),
                mm_to_meter(float(30)),
                mm_to_meter(float(30)),
                ])

q10 = np.array([0,mm_to_meter(float(30)),
                mm_to_meter(float(0)),
                mm_to_meter(float(10)),
                ])
            



#Plot Scale
x1 = -.5
x2 = .5
y1 = -.5
y2 = .5
z1 = 0
z2 = .5


# CARTESIAN Commands
tradj1 = rtb.jtraj(q0,q1,50)
tradj2 = rtb.jtraj(q1,q2,50)
tradj3 = rtb.jtraj(q2,q3,50)
tradj4 = rtb.jtraj(q3,q4,50)
tradj5 = rtb.jtraj(q4,q5,50)
tradj6 = rtb.jtraj(q5,q6,50)
tradj7 = rtb.jtraj(q6,q7,50)
tradj8 = rtb.jtraj(q7,q8,50)
tradj9 = rtb.jtraj(q8,q9,50)
tradj10 = rtb.jtraj(q9,q10,50)
tradj11 = rtb.jtraj(q10,q0,50)



CARTESIAN.plot(tradj1.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj2.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj3.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj4.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj5.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj6.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj7.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj8.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj9.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj10.q, limits=[x1,x2,y1,y2,z1,z2])
CARTESIAN.plot(tradj11.q, limits=[x1,x2,y1,y2,z1,z2])


CARTESIAN.teach(jointlabels=1)
