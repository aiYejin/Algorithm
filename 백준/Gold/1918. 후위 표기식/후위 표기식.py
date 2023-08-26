eq = list(input().rstrip())
stack = list()
for a in eq:
    if a.isalpha():
        print(a, end='')
    else:
        if a == '(':
            stack.append(a)
        elif a == ')':
            while stack[-1]!='(':
                print(stack.pop(), end='')
            stack.pop()
        elif a == '*' or a == '/':
            if len(stack) == 0 or stack[-1] == '-' or stack[-1] == '+':
                stack.append(a)
            else:
                while stack and stack[-1]!= '(' and stack[-1]!='+' and stack[-1]!='-':
                    print(stack.pop(),end='')
                stack.append(a)
        elif a == '-' or a == '+':
            while stack and stack[-1]!='(':
                print(stack.pop(), end='')
            stack.append(a)
while stack:
    print(stack.pop(), end='')