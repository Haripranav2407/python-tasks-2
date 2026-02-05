n = int(input("Enter number: "))
temp = n
while temp >=10:
    temp //= 10
first = temp
last = n % 10
if first != 0 and last %2 == 0:
    print("Valid")
else:
    print("Not valid")    