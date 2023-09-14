str1 = input("Enter a string: ")
str2 = input("Enter a string: ")

found =0
notfound =0

len1 = len(str1)
len2 = len(str2)

if len1 == len2:
    for i in range(len1):
        found=0
        for j in range(len1):
            if str1[i] == str2[j]:
                found = 1
                break
        if found ==0:
            notfound = 1
            break
    if notfound == 1:
        print("Not Anagram")
    else:
        print("Anagram")
else:
    print("not anagram")
    
    
