N = int(input())
i=1
while(1):
    if N-i>i:
        N-=i
    else:
        print(i)
        break
    i+=1