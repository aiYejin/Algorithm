p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

if p1[0]==p2[0]:
    x = p3[0]
elif p1[0]==p3[0]:
    x = p2[0]
else:
    x = p1[0]
if p1[1]==p2[1]:
    y = p3[1]
elif p2[1]==p3[1]:
    y = p1[1]
else:
    y = p2[1]
print(x, y)