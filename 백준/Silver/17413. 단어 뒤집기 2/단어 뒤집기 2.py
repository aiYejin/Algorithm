import sys
input = sys.stdin.readline
S = input().strip()
stack = list()
a=0
while a < len(S):
    if S[a] == "<":
        print("".join(stack), end='')
        stack.clear()
        print(S[a], end='')
        while S[a]!=">":
            a+=1
            print(S[a], end='')
    elif S[a]==' ':
        print("".join(stack), end='')
        stack.clear()
        print(" ", end='')
    else:
        stack.insert(0, S[a])
    a+=1
print("".join(stack), end='')

