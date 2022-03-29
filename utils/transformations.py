import numpy as np


def Rx(theta):
    return np.array([[ 1, 0            , 0            ],
                     [ 0, np.cos(theta),-np.sin(theta)],
                     [ 0, np.sin(theta), np.cos(theta)]])
  
def Ry(theta):
    return np.array([[ np.cos(theta), 0, np.sin(theta)],
                     [ 0            , 1, 0            ],
                     [-np.sin(theta), 0, np.cos(theta)]])
  
def Rz(theta):
    return np.array([[ np.cos(theta), -np.sin(theta), 0 ],
                     [ np.sin(theta), np.cos(theta) , 0 ],
                     [ 0            , 0             , 1 ]])

def rotation_xyz(x, y, z):
    return Rx(x)*Ry(y)*Rz(z)

def deg2rad(deg):
    return deg * np.pi / 180

# this is defined by rotation and translation
TRANSFORMATIONS = {0: ((0,0,0), (0,0,0)),
                   1: ((deg2rad(45), 0, 0), (3,2,1)),
                   2: ((deg2rad(45), deg2rad(-45), 0), (-2, 3, -1)),
                   3: ((deg2rad(-45), deg2rad(45), deg2rad(60)), (4, 7, 14)),
                   4: ((deg2rad(-120), deg2rad(120), deg2rad(180)), (7, 3, -1)),
                   5: ((deg2rad(120), deg2rad(-120), deg2rad(90)), (-7, -3, 1)),}

TRANSFORMATIONS = {k:{'rotation': rotation_xyz(*v[0]), 'translation': np.array(v[1]).reshape(3,1)} for k,v in TRANSFORMATIONS.items()}