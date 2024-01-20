N = int(input())
word = input()
arr = []
answer = 0
for _ in range(N-1):
    a = input()
    tmp = word
    for w in word:
        if a.find(w) != -1:
            a = a.replace(w,'',1)
            tmp = tmp.replace(w,'',1)
    if len(a) <= 1 and len(tmp) <= 1:
        answer +=1
print(answer)