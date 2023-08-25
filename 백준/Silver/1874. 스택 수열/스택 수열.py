import sys
input = sys.stdin.readline

n = int(input())
stack = list()
nums = list()
answer = list()
last = 1
flag = 1
for _ in range(n):
    number = int(input())
    nums.append(number)
for number in nums:
    if number < last:
        if stack[-1] != number:
            flag = 0
            break
        else:
            answer.append("-")
            del stack[-1]
    else:
        while last <= number:
            answer.append("+")
            stack.append(last)
            last+=1
        
        del stack[-1]
        answer.append("-")
if flag ==1:
    for i in answer:
        print(i)
else:
    print("NO")