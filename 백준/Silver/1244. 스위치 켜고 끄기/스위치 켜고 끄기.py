import sys
input = sys.stdin.readline

def Toggle(arr, idx):
    if arr[idx] == 1:
        arr[idx] = 0
    else:
        arr[idx] = 1
N = int(input())
arr = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        idx = b - 1
        while(idx<N):
            Toggle(arr, idx)
            idx += b
    else:
        for i in range(1, N):
            if b-1-i < 0 or b-1+i>=N or arr[b-1-i]!=arr[b-1+i]:
                Toggle(arr, b-1)
                for j in range(1,i):
                    Toggle(arr, b-1+j)
                    Toggle(arr, b-1-j)
                break
for i in range(N):
    print(arr[i], end=' ')
    if i%20 == 19:
        print()