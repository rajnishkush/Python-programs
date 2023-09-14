emp = [
    ('Alice', 'E001', 'Manager', 60000),
    ('Bob' , 'E002', 'Developer', 55000),
    ('Charlie', 'E003', 'Designer', 50000),
    ('Danniel', 'E004', 'HR', 80000),
]

sum = 0
for i in emp:
    for j in i[:-2:-1]:
            sum = sum + j
print(sum)

add = 0
for i in emp:
     for j in i:
        if type(j) is int:
            add = add + j
print(add)
