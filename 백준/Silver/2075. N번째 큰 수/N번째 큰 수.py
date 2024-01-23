import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(q) < N:
            heapq.heappush(q, num)
        elif num > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, num)
print(q[0])
