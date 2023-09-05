import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for g in graph[now]:
        if distance[g] == -1:
            distance[g] = distance[now] + 1
            q.append(g)

check = 0
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = 1

if check == 0:
    print("-1")
