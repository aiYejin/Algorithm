from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(q) < N:
            heappush(q, num)
        elif q[0] < num:
            heappop(q)
            heappush(q, num)
print(heappop(q))