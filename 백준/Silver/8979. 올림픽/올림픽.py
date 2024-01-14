import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
k = arr[K-1]
arr.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)

for i in range(N):
    if arr[i] == k:
        print(i+1)
        break