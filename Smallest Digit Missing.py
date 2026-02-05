n = int(input("Enter the number; "))
digits = 0
while digits <=9:
    temp = n
    found = False
    while temp > 0:
        digit = temp %10
        if digit == digits:
            found = True
            break
        temp //=10
    if not found:
        print(digits)
        break 
    digits+=1   