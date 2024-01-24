from collections import deque
N, M, V = map(int, input().split())
grid = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    grid[a][b] = grid[b][a] = 1
visited = [0] * (N+1)

def dfs(V):
    print(V, end = ' ')
    visited[V] = 1
    for i in range(N+1):
        if grid[V][i] == 1 and visited[i] == 0:
            dfs(i)
def bfs(V):
    q = deque([V])
    visited[V] = 0
    while q:
        V = q.popleft()
        print(V, end = ' ')
        for i in range(N+1):
            if grid[V][i] == 1 and visited[i] == 1:
                q.append(i)
                visited[i] = 0
dfs(V)
print()
bfs(V)