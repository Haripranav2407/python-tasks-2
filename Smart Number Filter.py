N = int(input("Enter Number(s): "))
temp = N
sum1  = 0
while temp > 0:
    digit = temp%10
    if digit ==2 or digit ==3 or  digit ==5 or digit ==7 :
        sum1+= digit
    temp = temp//10
print(sum1)    