def solution(picks, minerals):
    answer = 0
    #다이아:0 철:1 돌:2 
    stamina=[[1,1,1],[5,1,1],[25,5,1]]
    pick=[]
    for i in range(len(picks)):
        for _ in range(picks[i]):   #개수만큼
          pick.append(i)
    #다이아,철,돌곡괭이 순으로 정렬
    pick.sort()
          
    #필요한 곡괭이 수
    needs=0
    if len(minerals)%5==0:needs=len(minerals)//5
    else:needs=len(minerals)//5+1
    
    #만약 (필요한 곡괭이 수)보다 (가지고 있는 곡괭이)들이 더 많다면
    if needs<len(pick):pick=pick[:needs]
    #광물들이 더 많다면
    elif needs>len(pick):minerals=minerals[:len(pick)*5]
    
    #광물 5개씩 묶어서 돌곡괭이 기준 제일 피로도 높은 묶음 순으로 정렬
    for i in range(len(minerals)):
        if minerals[i]=='diamond':minerals[i]=25
        elif minerals[i]=='iron':minerals[i]=5
        elif minerals[i]=='stone':minerals[i]=1
    groups=[minerals[i:i+5] for i in range(0,len(minerals),5)]
    groups.sort(key=sum,reverse=True)
    
    for i in range(len(pick)):
        p=pick[i]
        for j in range(len(groups[i])):
            if groups[i][j]==25:answer+=stamina[p][0]
            elif groups[i][j]==5:answer+=stamina[p][1]
            elif groups[i][j]==1:answer+=stamina[p][2]
        
    return answer