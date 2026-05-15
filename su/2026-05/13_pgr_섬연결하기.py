'''
mst
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용

모든 섬을 연결하는 것이기 때문에
제일 싼 간선으로 연결하는 것이 이득임

'''

def solution(n, costs):
    answer = 0
    parents = list(range(n))
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        
        return parents[x]
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        parents[ra] = rb
        
    
    costs.sort(key=lambda x: (x[2], x[0], x[1]))

    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find(a) == find(b):  # 사이클 형성됐는지 루트 기준으로 비교
            continue
        union(a, b)
        answer += cost
        
        
    return answer

