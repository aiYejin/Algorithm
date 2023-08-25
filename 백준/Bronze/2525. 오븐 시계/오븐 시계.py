A, B = map(int, input().split())
C = int(input())
h = C // 60
m = C % 60
if B+m>59:
    h+=1
    B=(B+m)%60
else:
    B+=m
if A+h>23:
    A=(A+h)%24
else:
    A+=h
print(A, B)