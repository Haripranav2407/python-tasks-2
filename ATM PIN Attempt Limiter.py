n = int(input("enter pin: "))
i = 0
while i < 3:
    y = int(input("Enter correct pin:"))
    if y == n:
        print("Access granted")
        break
    i+=1
else:
    print("Cards blocked")    