import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([1, 3])

# On adding or any other such operation upper code will through an error
# because niether array's shape matches nor [1,3](as a smaller array) can
# be expand to larger 2d array like we did in previous code as 2nd
# Rule(expanding element) of broadcasting.

# So, here is the case of Incompatible shapes(third rule).
# And, its solution is reshaping that we already understood.

new_2d_arr = array_1d.reshape(2, 1)
# now numpy will brodcast [1] as a row to [1,2,3]
# and similarly, [3] as a row to [4,5,6], like
# expanding element

print(array_2d)
print(new_2d_arr)

result = new_2d_arr + array_2d

print(result)
