import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    answer = "YES"
    cnt = 0
    VPS = input().strip()
    for i in VPS:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            answer = "NO"
            break
    if cnt != 0:
        answer = "NO"
    print(answer)