H, M = map(int, input().split())
if M-45<0:
    H-=1
print((H+24)%24, (M+15)%60)