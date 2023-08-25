T = int(input())
for _ in range(T):
    n = int(input())
    sch = dict()
    for _ in range(n):
        s, num = input().split()
        sch[s]=int(num)
    print(max(sch, key=sch.get))