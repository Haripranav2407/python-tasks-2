b = int(input("Enter battery percentage: "))
d = int(input("Enter battery drop: "))
count = 0
if b < 20:
    print(0)
else:    
    while b >=20 :
        count+=1
        b = b - d
    print(count)  