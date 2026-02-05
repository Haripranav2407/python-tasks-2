w = float(input("Enter weight in kilograms: "))
p = float(input("enter price: "))
total = p * w
if w > 10:
    discount = total * 0.05
    price = total - discount
else:
    price = total
print(price)        