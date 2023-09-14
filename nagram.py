str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
 
if(len(str1)!=len(str2)):
    print("not anagram")
else:
    c = 0
    for i in str1:
        for j in str2:
            if (i==j):
                c+=1
    if (c==len(str1)):
        print("anagram")
    else:
        print("not anagram")
    
    
