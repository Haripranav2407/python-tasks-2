n = int(input("Enter the number: "))
temp = n
sum1 = 0
while temp > 0:
    digits =  temp %10
    sum1+=digits
    temp//=10
if sum1 %9 == 0:
    print("Valid")
else:
    print("Invalid")    

