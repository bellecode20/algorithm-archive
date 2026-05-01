def solution(tickets):
    answer = []
    
    def dfs(visited,temp,target):   #방문처리,경로,다음목적지
        nonlocal answer
        
        if len(temp)==len(tickets)+1:   #티켓을 다 사용했다면
            if not answer or temp<answer:   #아직 answer이 비어있거나/알파벳이 더 앞설때
                answer=temp
            return
        
        for i in range(len(tickets)):
            if visited[i]:continue  #이미 사용한 티켓이면
            if tickets[i][0]==target:   #티켓의 출발지가 가려는 목적지면
                visited[i]=True
                dfs(visited,temp+[tickets[i][1]],tickets[i][1])
                visited[i]=False
                
    visit=[False]*len(tickets)        
    for i in range(len(tickets)):
        if tickets[i][0]=="ICN":    #출발지가 "ICN"이면
            visit[i]=True   #i번째 티켓 사용처리
            dfs(visit,["ICN",tickets[i][1]],tickets[i][1]) #방문처리,경로,다음목적지
            visit[i]=False
    
    
    return answer