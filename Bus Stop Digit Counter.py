N = int(input("Enter the number(s): "))
temp = N
eve_cnt,odd_cnt = 0,0
while temp > 0:
    digit = temp%10
    if digit % 2 == 0:
        eve_cnt +=1
    else:
        odd_cnt+=1
    temp = temp//10
print(eve_cnt,odd_cnt)