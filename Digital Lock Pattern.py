n = int(input("Enter the number: "))
temp = n
last = n%10
count = 0
while temp > 0:
    digits = temp % 10
    if digits == 0:
        count+=1
    temp //=10
if last == 5 and count > 0:
    print("Open")
else:
    print("Locked")  