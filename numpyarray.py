import numpy as np

arr = np.array([10,21,23,14,15])
b = arr[0]

print(arr)
for i in range(1,5):
    if(b<=arr[i]):
        b = arr[i]
print("Biggest =",b)
print("Biggest =",max(arr))
