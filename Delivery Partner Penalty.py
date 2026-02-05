late = int(input("Enter time in minutes: "))
if late <= 10:
    penalty = 0
elif 11 <= late <= 30 :
    penalty = 50
else:
    penalty = 100
print(penalty)        