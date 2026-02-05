n = int(input("Enter the number: "))
count = 0
num = 1
while num <= n:
    temp = num
    has_four = False
    while temp > 0 :
        digit = temp %10
        if digit == 4:
            has_four = True
            break
        temp //=10
    if not has_four:
        count+=1
    num+=1    
print(count)            

    

