age = int(input("Enter the age: "))
price = 200
if age < 5:
    final = 0
elif 5 <= age <= 12:
    final = price*0.5
elif 13<= age <= 59:
    final = price
else:
    final = price*0.7
print(f"Final Ticket Price is ₹{final}")