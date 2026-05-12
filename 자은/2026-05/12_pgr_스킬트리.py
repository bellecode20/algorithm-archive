def solution(skill, skill_trees):
    answer = 0
    
    for sk in skill_trees:
        turn=0
        success=True
        for s in sk:
            if s in skill:
                if s != skill[turn]:
                    success=False
                    break
                else:
                    turn+=1
        if success:
            answer+=1
    return answer