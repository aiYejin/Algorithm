import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 21):
        for j in range(i, 21):
            if arr[i] > arr[j]:
                cnt += 1
    print(arr[0], cnt)