n = int(input("Enter the number: "))
temp = n
count,sum1 = 0,0
while temp > 0:
    digits = temp %10
    count+=1
    sum1+=digits
    temp //=10
if count == 4 and  sum1 > 15:
    print("Access granted") 
else:
    print("Accesess denied")  