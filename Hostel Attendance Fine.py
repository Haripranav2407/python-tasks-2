a = int(input("Enter attendance percentage: "))
if a < 75:
    fine = (75 - a)*10
else:
    fine = 0
print(fine)   