from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    q_sets = [set(x) for x in q]
    # print(q_sets)
    
    for cand in combinations(range(1, n + 1), 5):
        cand_set = set(cand)
        
        ok = True
        for i in range(len(q)):
            if len(cand_set & q_sets[i]) != ans[i]:
                ok = False
                break
        
        if ok:
            answer += 1
    
    return answer