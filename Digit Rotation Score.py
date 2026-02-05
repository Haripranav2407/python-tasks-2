N = int(input("Enter the number: "))
temp = N
rev = 0
while temp > 0:
    num = temp %10
    rev = rev*10 + num
    temp //=10
sum1 = N + rev
print(sum1)