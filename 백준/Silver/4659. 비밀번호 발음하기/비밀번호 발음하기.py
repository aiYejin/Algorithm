import sys
input = sys.stdin.readline

set_a = set(['a', 'e', 'i', 'o', 'u'])
set_b = set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'])

while True:
    command = input().rstrip()
    if command == 'end':
        break
    if len(set(command)&set_a)==0:
        print(f"<{command}> is not acceptable.")
        continue
    ex = []
    flag = True
    for c in command:
        ex.append(c)
        if len(ex) == 1:
            continue
        if ex[-1] == ex[-2] and c != 'e' and c != 'o':
            print(f"<{command}> is not acceptable.")
            flag = False
            continue
        if len(ex) > 3:
            ex.remove(ex[0])
        if len(ex) == 3 and (set(ex)&set_a == set(ex) or set(ex)&set_b == set(ex)):
            print(f"<{command}> is not acceptable.")
            flag = False
            continue
    if flag == True:
        print(f"<{command}> is acceptable.")