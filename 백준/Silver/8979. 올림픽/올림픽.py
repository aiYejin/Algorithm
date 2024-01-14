import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
for a in arr:
    if a[0] == K:
        k = [a[1],a[2],a[3]]
arr.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if [arr[i][1], arr[i][2], arr[i][3]] == k:
        print(i+1)
        break