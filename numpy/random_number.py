import numpy as np

# rng = np.random.default_rng(seed = 1)
# print(rng.integers(low= 1 ,high= 101, size= (3,4)))

# np.random.seed()
# print(np.random.uniform(low= -1 , high=1 ,size= (3,2)))


# rng = np.random.default_rng()
# array = np.array([1, 2, 3,4, 5, 6])
# rng.shuffle(array)
# print(array)

rng = np.random.default_rng()
fruits = np.array(['apple', 'banana', 'cherry', 'date'])
random_fruit = rng.choice(fruits, size= 2)
print(random_fruit)