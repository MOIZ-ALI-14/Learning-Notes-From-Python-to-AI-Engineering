# Filtering or Bolean Masking

import numpy as np

my_array = np.array([222, 444, 555, 666, 777, 888, 999])
print(my_array[my_array % 2 == 0])  # will print all even elements

# we use filtering or boolean masking when we want to access elements of an array that 
# satisfy a certain condition. In this case, we are accessing all the even elements of 
# the array `my_array`. The output will be: [222 444 666 888]