def solution(rows, columns, queries):
    answer = []
    arr=[[0]*columns for _ in range(rows)]
    
    num=1
    for i in range(rows):
        for j in range(columns):
            arr[i][j]=num
            num+=1
    
    def solve(x1,y1,x2,y2):
        cur=arr[x1][y1] #현재값
        mn=cur
        
        #위쪽변→
        for c in range(y1,y2):
            nxt=arr[x1][c+1]    #다음값 미리 백업
            arr[x1][c+1]=cur    #다음칸에 현재값으로 변경
            cur=nxt             #현재값을 다음값으로 갱신
            mn=min(mn,cur)
        
        #오른쪽변↓
        for r in range(x1,x2):
            nxt=arr[r+1][y2]
            arr[r+1][y2]=cur
            cur=nxt
            mn=min(mn,cur)
            
        #아래쪽변←
        for c in range(y2,y1,-1):
            nxt=arr[x2][c-1]
            arr[x2][c-1]=cur
            cur=nxt
            mn=min(mn,cur)
        
        #왼쪽변↑
        for r in range(x2,x1,-1):
            nxt=arr[r-1][y1]
            arr[r-1][y1]=cur
            cur=nxt
            mn=min(mn,cur)
        
        answer.append(mn)
        
    for r1,c1,r2,c2 in queries:
        solve(r1-1,c1-1,r2-1,c2-1)
        
    return answer