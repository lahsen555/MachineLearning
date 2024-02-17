import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

# this is the dataset, its actaully the grads of my classmates 
datay = [12.942 ,12.9, 14.328, 14.814, 15.12, 13.892, 13.495, 11.995, 11.495, 14.183, 14.145, 13.647, 14.531, 14.825, 13.647, 13.967, 12.172,
14.222, 14.939, 13.767, 15.197, 14.545, 13.283, 12.253, 12.772, 12.706, 13.27, 13.692]

# we store the data before plotting it 
datay.sort()
datax = [i for i in range(len(datay))]

# ploting the dataset 
# plt.scatter(datax, datay)

# now we have to create the model 
a = 0
b = 0
for i in range(1000):
    for x in datay: 
        model = a * x + b
        

# alright so let us try to plot the cost function, yeah we will vary a and b and see what we can get
def costf(a, b):
    sum = 0
    for x in datax:
        hx = a * x + b
        sum = sum + (hx - datay[x])**2
        
    return sum / (2 * len(datay))

        
a_values = np.linspace(-10, 10, 100)
b_values = np.linspace(-10, 10, 100)

a_mesh, b_mesh = np.meshgrid(a_values, b_values)

# now the code is workig but we just need to know what each part is doing yeah 
cost_values = np.array([[costf(a, b) for a, b in zip(a_row, b_row)] for a_row, b_row in zip(a_mesh, b_mesh)])

# now we can plot this data

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


surf = ax.plot_surface(a_mesh, b_mesh, cost_values, cmap='viridis')

fig.colorbar(surf)

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('cost')

plt.show()

# don't forge that we have done all of this just to plot the 3d shape but we are not interested in this stuff 