import numpy as p

arr = p.array([1,2,3,4,5,6,7,8,9])

#7,1,4,5,6
#2,5,1,6,4
#1,5,4,3,2
#1,2,7,3,4

a = arr.reshape(3,3)

for i in range(1,5):
    for j in range(1,i):
        print("*")
    print("\n")
