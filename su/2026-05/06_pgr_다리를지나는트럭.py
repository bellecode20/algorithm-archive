# 14:33 ~ 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    trucks = deque([])  # 대기 트럭
    bridge = deque([])  # 다리 위
    
    time = 0
    print(truck_weights)
    while True:
        # 다리 위에 아무것도 없으면 넣기
        if not bridge:
            bridge.append((time, truck_weights.popleft()))
        break
                
        
    answer += len(bridge) + time
    # 다리 위에 있는 애들 더하기
    return answer

print(solution(100, 100, [10]))
