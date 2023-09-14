import numpy as p;

arr = p.array([1,2,3,4,5,6,6,7,8]);
a = arr.reshape(3,3);

sum = 0

i=0
while i<len(a):
    j = 0
    while j<len(a[i]):
        if i == j:
            sum+= a[i][j]

print(sum)

