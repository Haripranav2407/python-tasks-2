n = int(input("Enter the distance: "))
if 1<= n <= 5:
    fare = 10 * n
elif 6 <= n <= 15:
    fare = 8 *n
else:
    fare = 6*n
print(fare)        