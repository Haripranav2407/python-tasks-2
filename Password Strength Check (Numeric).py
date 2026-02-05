N = int(input("Enter password: "))
temp = N
count = 0
has_seven = False
while temp > 0:
    digit = temp % 10
    count += 1
    if digit == 7:
        has_seven = True
    temp //= 10
if count >= 6 and has_seven:
    print("STRONG")
else:
    print("WEAK")