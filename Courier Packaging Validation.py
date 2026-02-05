l = int(input("Length: "))
w = int(input("width: "))
h = int(input("height: "))

total = l+w+h

if l>0 and w > 0 and h > 0 and total <=150:
    print("Accepted")
else:
    print("Rejected")    