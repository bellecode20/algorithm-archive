'''
pgr 다리를 지나는 트럭

입력:
bridge_length
weight
truck_weights

구조:
큐로 앞에꺼 하나씩 pop
올릴ㄹ 수 있으면 넣고 아님 0
time +1
'''

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()

    for i in range(bridge_length):
        bridge.append(0)

    idx = 0
    time = 0
    cur = 0

    while idx < len(truck_weights):
        out = bridge.popleft()
        cur -= out

        if cur + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            cur += truck_weights[idx]
            idx += 1
        else:
            bridge.append(0)
        time += 1

    return time + bridge_length