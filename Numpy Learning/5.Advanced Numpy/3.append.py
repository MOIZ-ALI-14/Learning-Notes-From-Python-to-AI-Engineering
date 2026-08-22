# append() is used to add one or multiple elements at the end of array
# same like insert, append also doesn't change original array but
# creates a new array

import numpy as np

my_array = np.array([12, 13, 14, 15])
print(my_array)
new_array = np.append(my_array, [18, 19, 20])
print(new_array)

# we use append when we want to add elements at the end of array
