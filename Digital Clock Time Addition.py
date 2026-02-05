H = int(input("Enter hours: "))
M = int(input("Enter minutes: "))
X = int(input("Enter minutes to add: "))
total_minutes = M + X
H = H + (total_minutes // 60)
M = total_minutes % 60
H = H % 24
print(H, M)