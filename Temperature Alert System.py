n = int(input("Enter the num: "))
i = 0
while i < n:
    r = int(input("enter temp: "))
    if r > 45:
        print("Alert")
        break
    i+=1
else:
    print("Safe")