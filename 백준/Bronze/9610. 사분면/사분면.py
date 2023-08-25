T = int(input())
q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0
axis = 0
for _ in range(T):
    a, b = map(int, input().split())
    if a==0 or b==0:
        axis += 1
    elif a>0 and b>0:
        q_1 += 1
    elif a<0 and b>0:
        q_2 += 1
    elif a<0 and b<0:
        q_3 += 1
    elif a>0 and b<0:
        q_4 += 1
print(f"Q1: {q_1}")
print(f"Q2: {q_2}")
print(f"Q3: {q_3}")
print(f"Q4: {q_4}")
print(f"AXIS: {axis}")