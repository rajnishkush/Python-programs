import numpy as p;

arr = p.array([1,2,3,4,5,6,7,8,9]);
a = arr.reshape(3,3);

sum = 0;

for i in range(0,3):
    for j in range(0,3):
        if i ==j:
            continue;
        elif i+j ==2:
            continue;
        else:
            sum+=a[i][j];

print(sum);


