import sys
input = sys.stdin.readline
stack = list()
laser = input().strip()
flag = 0
answer = 0
for i in laser:
    if i == "(":
        stack.append(i)
        flag = 1
    else:
        if flag == 1:
            stack.pop()
            answer += len(stack)
            flag = 0
        else:
            stack.pop()
            answer+=1
print(answer)