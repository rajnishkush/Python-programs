#Write a code to store first 30 prime numbers in a list in reverse order

list = []
count=0
i=2
while(count<=30):
    j=2
    flag = 0 
    while(j<i):
        if (i%j==0):
            flag = 1
            break
        j+=1
    if(flag ==0):
        count +=1
        list.insert(0,i)
    i+=1
print(list)
        
