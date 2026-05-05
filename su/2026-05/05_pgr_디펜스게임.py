import heapq 

def solution(n, k, enemy):
    answer = 0
    total_len = len(enemy)
    enemy_hq = []
    heapq.heapify(enemy_hq)
    
    for i in range(total_len):
        if n < enemy[i]:  # 무적권 써야 하는 경우
            if k == 0:  # 더이상 무적권 없는 경우
                return i
            
            heapq.heappush(enemy_hq, (-enemy[i], i))
            max_value, max_idx = heapq.heappop(enemy_hq)
            max_value = abs(max_value)  # 양수로 변환
            n += max_value  # 무적권 쓴 거 플러스
            n -= enemy[i]  # 현재 적군 막기
            k -= 1
            

        else:  # 현재 있는 병사로 막을 수 있는 경우
            heapq.heappush(enemy_hq, (-enemy[i], i))
            n -= enemy[i]
            
    answer = i + 1
    return answer

print(solution(2, 4, [3, 3, 3, 3]))
# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
