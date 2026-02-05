n = int(input("enter the number: "))
sum1 = 0
pro = 1
temp = n
while temp > 0:
    digits = temp %10
    sum1+=digits
    pro*=digits
    temp //=10
if sum1 % 2 == 0 and pro %3 == 0:
    print("Valid")
else:
    print("Invalid")    