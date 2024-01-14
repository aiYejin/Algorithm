import sys
input = sys.stdin.readline

N, G = input().split()
s = set()
for _ in range(int(N)):
    s.add(input())
cnt = len(s)
if G == 'Y':
    print(cnt)
elif G == 'F':
    print(cnt//2)
elif G == 'O':
    print(cnt//3)