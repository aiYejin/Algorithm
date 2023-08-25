s = 0
for _ in range(5):
    score = int(input())
    if score >= 40:
        s += score
    else:
        s += 40
print(s//5)