t1 = (3,4,5)
t2 = (100,) # comma is mandatory otherwise it assumes t2 to be an int
print(t1+t2)

t3 = list(t1)
t3.append(100)
t4 = tuple(t3)
print(t4)
