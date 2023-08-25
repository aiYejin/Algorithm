T = int(input())
a = 0
b = 0
for _ in range(T):
    n = int(input())
    if n == 0:
        b+=1
    else:
        a+=1
if a>b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")