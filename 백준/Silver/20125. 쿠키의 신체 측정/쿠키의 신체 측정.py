import sys
input = sys.stdin.readline

N = int(input())
arr = list(list(input().rstrip()) for _ in range(N))
x, y = 0, 0
answer = []

for i in range(N):
    if '*' in arr[i]:
        for j in range(N):
            if x == 0 and y == 0 and arr[i][j] == '*':
                x, y = i+1, j
                break
        break

cnt = 0

for i in range(y):
    if arr[x][i] == '*':
        answer.append(y - i)
        break
for i in range(y+1,N):
    if arr[x][i] == '_':
        answer.append(i-y-1)
        break
if len(answer) == 1:
    answer.append(N-y-1)
for i in range(x+1,N):
    if arr[i][y] == '_':
        answer.append(i-x-1)
        break
for i in range(x+answer[-1]+1,N):
    if arr[i][y-1] == '_':
        answer.append(i-x-answer[-1]-1)
        break
if len(answer) == 3:
    answer.append(N-x-answer[-1]-1)
for i in range(x+answer[-2]+1,N):
    if arr[i][y+1] == '_':
        answer.append(i-x-answer[-2]-1)
        break
if len(answer) == 4:
    answer.append(N-x-answer[-2]-1)
print(x+1, y+1)
for a in answer:
    print(a, end=' ')