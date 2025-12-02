import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']
                   ]])
#is will raise an IndexErrorrint(array.ndim)
word = array[0, 0,0 ] +array[2,0,0] + array[1,1,2]
print(word)  # Output: L