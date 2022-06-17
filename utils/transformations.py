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
    sigma_angle = 1 * np.pi/180 # * (i//2+1)
    sigma_dist = 0.3 # * (i//2+1)
        
    TRANSFORMATIONS[i] = (tuple(rng.normal(0, sigma_angle, 3)), tuple(rng.normal(0, sigma_dist, 3)))

# for i in range(1, 11):
#     TRANSFORMATIONS[i] = ((i*np.pi/90, i*np.pi/90, i*np.pi/90), (0, 0, 0))

# for i in range(11, 21):
#     j = i-10
#     TRANSFORMATIONS[i] = ((0, 0, 0), (j*0.05, j*0.05, j*0.05))

# for i in range(21, 31):
#     j = i-20
#     TRANSFORMATIONS[i] = ((j*np.pi/90, j*np.pi/90, j*np.pi/90), (j*0.05, j*0.05, j*0.05))

TRANSFORMATIONS = {k:{'rotation': rotation_xyz(*v[0]), 'translation': np.array(v[1]).reshape(3,1)} for k,v in TRANSFORMATIONS.items()}