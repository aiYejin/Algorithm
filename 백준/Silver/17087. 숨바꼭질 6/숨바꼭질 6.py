def getGCD(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return getGCD(b, a%b)

N, S = map(int, input().split())
yng = list(map(int, input().split()))
distance = list()

for i in range(len(yng)):
    if yng[i]-S !=0 :
        distance.append(abs(yng[i]-S))
answer = 0
for i in range(0,len(distance)):
    if i == 0:
        answer = distance[i]
    answer = getGCD(answer, distance[i])
print(answer)