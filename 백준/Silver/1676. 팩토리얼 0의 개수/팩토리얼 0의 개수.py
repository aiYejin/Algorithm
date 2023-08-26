N = int(input())
ans = 1
answer = 0
for i in range(1, N+1):
    ans *= i
for i in range(len(str(ans))-1, -1, -1):
    if str(ans)[i] == '0':
        answer+=1
    else:
        break
print(answer)