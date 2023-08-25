import sys
input = sys.stdin.readline
T = int(input())
stack = list()
for _ in range(T):
    m = input().split()
    if m[0]=="push":
        stack.append(int(m[1]))
    elif m[0]=="pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
    elif m[0]=="size":
        print(len(stack))
    elif m[0]=="empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif m[0]=="top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[len(stack)-1])