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
    return Rx(x)@Ry(y)@Rz(z)


rng = np.random.default_rng(seed=1)
TRANSFORMATIONS = {0: ((0,0,0), (0,0,0))}
for i in range(1, 100):
    sigma_angle = np.pi/18 # 10 degrees
    sigma_dist = 0.1
        
    TRANSFORMATIONS[i] = (tuple(rng.normal(0, sigma_angle, 3)), tuple(rng.normal(0, sigma_dist, 3)))

TRANSFORMATIONS = {k:{'rotation': rotation_xyz(*v[0]), 'translation': np.array(v[1]).reshape(3,1)} for k,v in TRANSFORMATIONS.items()}