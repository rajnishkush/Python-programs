# Q2.  Tax Calculation

cp = int(input("Enter the cost price: "))
tax =0
         
if(cp<=50000):
    tax = cp*0.05
elif(cp > 50000 and cp <=100000):
    tax = 50000*0.05
    tax += (cp-50000)*0.1
else:
    tax = 50000*0.05
    tax += (cp-50000)*0.1
    tax += (cp-100000)*0.15

print("The tax amount is : ",tax)
