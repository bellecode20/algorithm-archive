def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    cam=routes[0][1]
    
    for i in range(1,len(routes)):
        if cam<routes[i][0] or cam>routes[i][1]:
            cam=routes[i][1]
            answer+=1
    
    return answer