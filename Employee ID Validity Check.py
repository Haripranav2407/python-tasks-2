N = int(input("Enter Id: "))
temp = N
count,sum1= 0,0
while temp > 0:
    digits = temp%10
    sum1+=digits
    count+=1
    temp //=10
if count == 6 and N %7 ==0:
    print("Valid")
else:
    print("Invalid")   