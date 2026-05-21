def solution(n, stations, w):
    answer = 0
    uninstalled=[]
    uninstalled.append(stations[0]-w-1)
    
    for i in range(1,len(stations)):
        length=(stations[i]-w)-(stations[i-1]+w)-1
        uninstalled.append(length)
    
    if stations[-1]+w < n:
        length=n-(stations[-1]+w)
        uninstalled.append(length)
    
    ran=2*w+1
    for l in uninstalled:
        if l%ran==0:
            answer+=l//ran
        else:
            answer+=l//ran+1

    return answer