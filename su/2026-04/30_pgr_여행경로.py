
from collections import defaultdict
answer = []
N = 0
cnt_dict = defaultdict(int)
visited = defaultdict(int)
graph = defaultdict(set)

def dfs(depth, history):
    global answer
    
    if answer:
        return
    
    if depth == N:
        answer = history
        return
    
    a = history[-1]
    for b in graph[a]:  
        key = (a, b)
        if key not in visited or visited[key] < cnt_dict[key]:
            visited[(key)] += 1
            dfs(depth + 1, history + [b])
            visited[(key)] -= 1


def solution(tickets):
    global N, graph
    
    N = len(tickets)
    
    for ticket in tickets:
        cnt_dict[tuple(ticket)] += 1
        graph[ticket[0]].add(ticket[1])

    for key, li in graph.items():
        graph[key] = sorted(list(graph[key]))  # 어차피 visited 하기 때문에 set으로 중복없애지 않아도 되기는 함


    dfs(0, ["ICN"])
    
    return answer

tc1 = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"]]
# 기대값: ["ICN", "COO", "ICN", "BOO"]
print(solution(tc1))