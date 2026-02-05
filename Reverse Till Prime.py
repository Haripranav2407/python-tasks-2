n = int(input("Enter number: "))
temp = n
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev <= 1:
    print("NOT PRIME")
else:
    i = 2
    is_prime = True

    while i < rev:
        if rev % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("PRIME")
    else:
        print("NOT PRIME")