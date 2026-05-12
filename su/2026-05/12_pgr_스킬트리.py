def solution(skill, skill_trees):
    answer = 0
    N = len(skill_trees)
    
    for i in range(N):
        cur = skill_trees[i]
        txt = ""
        
        for cha in cur:
            if cha not in skill:
                continue
            txt += cha
        
        cur_idx = 0  # 현재 해야하는 스킬
        is_okay = True
        
        for i in range(len(txt)):
            if txt[i] not in skill:
                continue
            
            if txt[i] != skill[cur_idx]:
                is_okay = False
                break
            cur_idx += 1
        
        if is_okay:
            answer += 1
            
    
    return answer
    

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))