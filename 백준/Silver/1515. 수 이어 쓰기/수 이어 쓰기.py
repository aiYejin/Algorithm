string = input()
N = 1
n = '1'
for s in string:
    while s not in n:
        N += 1
        n = str(N)
    n = n[n.find(s)+1:]
print(N)
