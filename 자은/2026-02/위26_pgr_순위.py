def solution(n, results):
    answer = 0
    record=[[False]*(n+1) for _ in range(n+1)]
    
    for w,l in results:
        record[w][l]=True
    
    #a가 b를 이기고, b가 c를 이기면, a가 c를 이긴다.
    for b in range(1,n+1):
        for a in range(1,n+1):
            for c in range(1,n+1):
                if record[a][b] and record[b][c]:
                    record[a][c]=True
    
    for i in range(1,n+1):
        win=lose=0
        for j in range(1,n+1):
            
            if record[i][j]:
                win+=1  #i가 j를 이겼으면
            elif record[j][i]:
                lose+=1   #j가 i를 이겼으면(=i가 j한테 졌으면)
        if win+lose==n-1:
            answer+=1

    return answer