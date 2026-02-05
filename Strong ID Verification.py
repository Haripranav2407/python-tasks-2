N = int(input("Enter the number: "))
temp = N
sum1 = 0
while temp > 0:
    fact = 1
    i = 1
    digits = temp%10
    while i <= digits:
        fact*=i
        i+=1
    sum1+=fact
    temp //=10
if sum1 == N:
    print("STRONG")
else:
    print("NOT STRONG")        