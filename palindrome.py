str = input("Enter a string ")

start = 0
end = len(str)-1

while(start<=end) :
    if str[start] == str[end]:
        pass
    else:
        print("Not palindrome ")
        break
    start+=1
    end-=1
if end <= start:
    print("palindrome")
