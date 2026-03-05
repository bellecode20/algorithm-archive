from collections import defaultdict

def solution(edges):
    # 각 노드별 들어오는/나가는 간선 수 기록
    # [in_count, out_count]
    counts = defaultdict(lambda: [0, 0])
    nodes = set()
    
    for u, v in edges:
        counts[u][1] += 1 # u에서 나감
        counts[v][0] += 1 # v로 들어옴
        nodes.add(u)
        nodes.add(v)
    
    created_node = 0
    donut, bar, eight = 0, 0, 0
    
    # 1. 생성된 정점 찾기
    for node in nodes:
        in_c, out_c = counts[node]
        if in_c == 0 and out_c >= 2:
            created_node = node
            break
            
    # 전체 그래프 개수 = 생성된 정점에서 뻗어나간 화살표 수
    total_graphs = counts[created_node][1]
    
    # 2. 각 노드의 특징으로 그래프 종류 판별
    for node in nodes:
        if node == created_node:
            continue
            
        in_c, out_c = counts[node]
        
        # 막대 그래프의 특징: 어느 한 노드는 나가는 게 없다 (종점)
        if out_c == 0:
            bar += 1
        # 8자 그래프의 특징: 어느 한 노드는 들어오는 게 2개, 나가는 게 2개다 (교차점)
        elif out_c == 2 and in_c >= 2:
            eight += 1
            
    # 3. 도넛 그래프는 계산으로 구함
    donut = total_graphs - bar - eight
    
    return [created_node, donut, bar, eight]