def solution(N, stages):
    answer = dict()
    people = len(stages)
    for i in range(1, N+1):
        if people == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i)/people
            people -= stages.count(i)
        
    return sorted(answer, key = lambda x:-answer[x])