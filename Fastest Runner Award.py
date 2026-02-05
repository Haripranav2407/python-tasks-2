N = int(input("Enter no of runners: "))
minimum = int(input("Enter time: "))
i = 1
while i < N:
    time = int(input("Enter time: "))
    if time < minimum:
        minimum = time
    i+=1
print("Minimum time: ",minimum) 