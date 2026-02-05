N = int(input("Enter number of days: "))
total = 0.0
i = 0
while i < N:
    rain = float(input("Enter rainfall: "))
    total += rain
    i += 1
average = total / N
print(average)