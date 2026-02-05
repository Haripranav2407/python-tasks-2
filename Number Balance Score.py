n=int(input("n:"))
digits=len(str(n))
half=digits // 2
div=10**half
a,b=n//div,n%div
s1=s2=0
while a:
    s1 += a % 10
    a//= 10
while b:
    s2 += b % 10
    b//= 10
if s1==s2:
    print("BALANCED")
else:
    print("unbalanced")
