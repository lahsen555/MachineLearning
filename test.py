import numpy as np

a_values = np.linspace(-5, 5, 4)
b_values = np.linspace(-5, 5, 4)

a_mesh, b_mesh = np.meshgrid(a_values, b_values)

print(a_values)
print("############################################")
print(b_values)  

# i can see now why they are the same space, its because they are evently spaced point 