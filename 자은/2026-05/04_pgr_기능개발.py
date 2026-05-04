def solution(progresses, speeds):
    answer = []
    times=[]    #각 작업당 걸리는 시간
    
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]:
            times.append((100-progresses[i])//speeds[i]+1)
        else:
            times.append((100-progresses[i])//speeds[i])
            
    stack=[]
    for i in range(len(times)):
        if stack: 
            if stack[0]>=times[i]:  #순서가 제일 앞인 작업이 나보다 더 오래걸릴때
                stack.append(times[i])
            else:   #내가 더 늦게 끝날때
                answer.append(len(stack))
                stack=[times[i]]
        else:
            stack.append(times[i])
            
    if stack:answer.append(len(stack))
            
    return answer