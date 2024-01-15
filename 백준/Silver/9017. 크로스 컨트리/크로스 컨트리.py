import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    set_arr = set(arr)
    answer = {}
    cnt = [0]*201
    for s in set_arr:
        if arr.count(s) != 6:
            arr = [i for i in arr if i != s]
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