import sys
input = sys.stdin.readline

N, s, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    scores.append(s)
    scores.sort(reverse = True)
    if len(scores) > P and scores[P] >= s:
        print(-1)
    else:
        print(scores.index(s)+1)
            