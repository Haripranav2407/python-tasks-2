balance=float(input("balance_amount:"))
with_drawl_amount=float(input("with drawl amount:"))
if(with_drawl_amount>balance and with_drawl_amount%100!=0 and balance-with_drawl_amount<500):
    print("rejected")
else:
    print("success")