n = int(input("Enter number: "))
count = 0
num = 2
while num <=n:
    i = 2
    is_prime = True
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i+=1
    if is_prime:
        count+=1
    num+=1
print(count)            