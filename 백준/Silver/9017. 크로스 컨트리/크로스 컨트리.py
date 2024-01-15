import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    answer = {}
    cnt = [0]*201
    arr = [0]*201
    team = [0]*201
    for a in scores:
        team[a] += 1
    for a in scores:
        if team[a] == 6:
            arr.append(a)
    for i in range(len(arr)):
        if cnt[arr[i]] == 0:
            answer[arr[i]] = [i,0,0]
        elif cnt[arr[i]] == 4:
            answer[arr[i]][1] = i
        elif cnt[arr[i]] == 5:
            answer[arr[i]][2] = i
        else:
            answer[arr[i]][0] += i
        cnt[arr[i]] += 1
    ans = sorted(answer.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))
    print(ans[0][0])