import numpy as np

arr_1d = np.array([10, 30, 50, 70, 90])
arr_2d = np.array([[10, 30, 50], [70, 90, 110]])
arr_3d = np.array([[[10, 30], [50, 70]], [[90, 110], [130, 150]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# ndim is an attribute of numpy arrays that returns the number of dimensions (or axes)
# of the array. It is useful for understanding the structure of the data and how it 
# can be manipulated or processed.