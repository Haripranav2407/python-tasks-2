A = int(input("Enter amount: "))
count = 0
count += A // 500
A %= 500
count += A // 200
A %= 200
count += A // 100
A %= 100
count += A // 50
A %= 50
count += A // 20
A %= 20
count += A // 10
A %= 10
count += A // 1
A %= 1
print(count)