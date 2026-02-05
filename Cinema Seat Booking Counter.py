s =int(input("Enter no of seats: "))
n = int(input("Enter total no of customers: "))
i = 0
while i < n:
    if s > 0:
        print("Booked")
        s-=1
    else:
        print("Housefull")
    i+=1
if s > 0:
    print("Remaining seats", s)    