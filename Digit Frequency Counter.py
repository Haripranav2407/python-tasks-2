n = int(input("Enter num: "))
d = int(input("Enter digit: "))
temp = n
count = 0
while temp > 0:
    digits = temp % 10
    if digits == d:
        count+=1
    temp //=10
print(count)        