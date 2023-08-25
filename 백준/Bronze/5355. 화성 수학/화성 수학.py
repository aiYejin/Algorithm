T = int(input())
for _ in range(T):
    answer = 0
    mars = list(input().split())
    for i in range(len(mars)):
        if i == 0:
            answer+=float(mars[i])
        else:
            if mars[i]=="@":
                answer*=3
            elif mars[i]=="%":
                answer+=5
            elif mars[i]=="#":
                answer-=7
    print("%0.2f" % answer)