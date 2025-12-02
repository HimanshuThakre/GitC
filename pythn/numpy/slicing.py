import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

#array[start:end:step]

print(array[:3, :3])  # Slicing rows 1 to 2 and columns 0 to 1