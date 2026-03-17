from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num=[i for i in range(1,n+1)]
    
    for comb in combinations(num,5):
        comb=set(comb)
        success=True
        for j in range(len(q)):
            if len(comb&set(q[j]))!=ans[j]: #교집합의 개수가 시스템응답이랑 다르면
                success=False
                break
        if success:
            answer+=1
            
    return answer