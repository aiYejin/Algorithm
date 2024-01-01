import sys
input = sys.stdin.readline

N = int(input())
a = 1
answer = 0
while N > 0:
    answer += 1
    N -= a
    if a == 1:
        a = 6
    else:
        a += 6
print(answer)