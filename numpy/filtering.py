import numpy as np

ages = np.array([[21,17,45,67,12,15,30],
                [39,50,29,18,23,41,33]])

# teenagers = ages[ages <18]

# adults = ages[(ages >=18)&(ages <=65)]
# seniors = ages[ages >=65]
# evens = ages[ages %2 ==0]
# odds = ages[ages %2 !=0]

# print(odds)
adults = np.where(ages >=18, ages, 0)
print(adults)