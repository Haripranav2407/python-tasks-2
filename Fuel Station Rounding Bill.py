l = float(input("Enter litre: "))
pri = float(input("Enter price: "))
final = int(l * pri)     
last_digit = final % 10

if last_digit <= 4:
    final = final - last_digit
else:
    final = final + (10 - last_digit)

print(final)