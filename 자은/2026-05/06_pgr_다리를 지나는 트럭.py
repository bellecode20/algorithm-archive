from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge=deque([0]*bridge_length)  #현재 다리위에 올라가있는 트럭들
    time=0
    sm=0    #현재 다리위에 있는 트럭들 무게
    trucks=deque(truck_weights)
    
    while bridge:
        time+=1
        sm-=bridge.popleft()
        
        if trucks:
            if sm+trucks[0]<=weight:
                t=trucks.popleft()
                bridge.append(t)
                sm+=t
            else:
                bridge.append(0)
            
    
    return time