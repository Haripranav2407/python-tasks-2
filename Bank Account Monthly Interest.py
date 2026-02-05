B = int(input("Enter balance: "))
if B < 10000:
    annual_rate = 0.03
elif B <= 50000:
    annual_rate = 0.05
else:
    annual_rate = 0.07
monthly_interest = (B * annual_rate) / 12
print(monthly_interest)