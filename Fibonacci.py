#write a program to store first 30 term of a fibo series in reverse order

list = []
i = 3
a = 0
b = 1

list.insert(0,a)
list.insert(0,b)

while(i<=28):
    c = a+b
    list.insert(0,c)
    a = b
    b= c
    i+=1
print (list)
    
    
