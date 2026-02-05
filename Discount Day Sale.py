amt = int(input("Enter the amount: "))
if amt < 1000:
    final = amt
elif 1000 <= amt <=2999 :
    final =amt -  amt *0.10    
elif 3000<= amt <=4999:
    final = amt - amt*0.2
else:
    final =amt - amt * 0.3    
final = int(final)
print(f"The total amount payable is {final}")