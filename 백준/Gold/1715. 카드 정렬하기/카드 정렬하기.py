import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
heap = []
answer = 0
for _ in range(N):
    heappush(heap, int(input()))
while len(heap) > 1:
    s = heappop(heap) + heappop(heap)
    answer += s
    heappush(heap, s)
print(answer)