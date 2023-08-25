s=int(input())
a=s//300
b=(s%300)//60
c=(s%60)//10
s%=10
if s>0:
    print("-1")
else:
    print(a, b, c)