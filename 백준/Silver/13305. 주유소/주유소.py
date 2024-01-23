import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0
min_c = cost[0]
for i in range(N-1):
    min_c = min(min_c, cost[i])
    answer += distance[i]*min_c
print(answer)