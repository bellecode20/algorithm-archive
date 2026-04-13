def solution(picks, minerals):
    answer = int(1e9)
    cost_info = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]  # 다이아, 철, 돌
    mineral_idx = {
        "diamond": 0,
        "iron": 1,
        "stone": 2,
    }
    
    def dfs(depth, cost, history):
        nonlocal answer
        
        if depth >= len(minerals):
            answer = min(answer,  cost)
            return
        
        no_tool = True
        for tool in range(3):
            if visited[tool] == picks[tool]:  # 다 사용한 경우
                continue
                
            no_tool = False
            visited[tool] += 1
            
            new_cost = cost
            for i in range(depth, depth + 5):
                if i >= len(minerals): # 미네랄 순서보다 넘어가면 끝
                    break
                idx = mineral_idx[minerals[i]]  # 캐야하는 미네랄
                new_cost += cost_info[tool][idx]
            
            dfs(i + 1, new_cost, history + [tool])
            visited[tool] -= 1
        
        if no_tool: # 더 사용할 곡괭이가 없음
            answer = min(answer,  cost)
            return
        
    visited = [0] * 3
    dfs(0, 0, [])

    return answer