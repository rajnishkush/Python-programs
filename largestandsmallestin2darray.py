import numpy as p;

a = p.array([[-12,20,32],[14,-85,76],[17,38,59]])
max = min = a[0][0];

for i in a:
    for j in i:
        if j > max:
            max = j
        if j < min:
            min = j
print('max = ',max)
print('min = ',min)

print(p.__version__)
