A, B, C=map(int, input().split())
D = int(input())
h = D//3600
s = D%60
m = D//60%60
if C+s>59:
    m+=1
C=(C+s)%60
if B+m>59:
    h+=1
B=(B+m)%60
A=(A+h)%24
print(A, B, C)