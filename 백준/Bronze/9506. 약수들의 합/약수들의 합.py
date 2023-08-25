while(1):
    n = int(input())
    s = list()
    if n == -1:
        break
    for i in range(1,n//2+1):
        if n%i==0:
            s.append(i)
        if sum(s)>n:
            break
    if sum(s) == n:
        print(f"{n} = ", end='')
        for i in range(len(s)):
            if i == 0:
                print(f"{s[i]}", end='')
            else:
                print(f" + {s[i]}",end='')
        print()
    else:
        print(f"{n} is NOT perfect.")