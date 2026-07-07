from collections import Counter

def solution(k, tangerine):
    answer = 0
    groups = Counter(tangerine)
    sorted_groups = sorted(groups.items(), key = lambda x: (-x[1]))
    cnt = 0
    
    for i in range(len(sorted_groups)):
        _, group_cnt = sorted_groups[i]
        
        cnt += group_cnt # 귤의 개수
        answer += 1  # 귤 종류
        
        if cnt >= k:
            break
        
    
    return answer