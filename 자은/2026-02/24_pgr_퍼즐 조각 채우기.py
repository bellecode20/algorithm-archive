from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#각 빈공간/각 조각 생김새
def find_p(lst,target):
    all_p=[]
    visited=[[False]*len(lst) for _ in range(len(lst))]
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j]==target and not visited[i][j]:
                piece=[]    #한 조각의 좌표들을 담을 리스트
                q=deque([(i,j)])
                visited[i][j]=True
                
                while q:
                    cx,cy=q.popleft()
                    piece.append((cx,cy))
                    
                    for d in range(4):
                        nx,ny=cx+dx[d],cy+dy[d]
                        if nx<0 or nx>=len(lst) or ny<0 or ny>=len(lst) or visited[nx][ny]:
                            continue
                        if lst[nx][ny]==target:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                mnr=min(r for r,c in piece)
                mnc=min(c for r,c in piece)
                
                piece = sorted([(r - mnr, c - mnc) for r, c in piece])
                all_p.append(piece)
    return all_p

#조각 1개 90도 회전
def rotate(lst):
    r90=[]
    for i in range(len(lst)):
        r,c=lst[i]
        r90.append((c,-r))
        
    mn_r=min(c for r,c in r90)
    mn_c=min(c for r,c in r90)
    
    r90=sorted([(r - mn_r, c - mn_c) for r, c in r90])
    return r90
        

def solution(game_board, table):
    answer = 0
    
    
    empty=find_p(game_board,0)  #(순회할 리스트,찾을 값)
    all_p=find_p(table,1)
    used=[False]*len(all_p) #조각 사용여부
    

    for e in empty:
        for i in range(len(all_p)):
            sucess=False
            for _ in range(4):
                if e==all_p[i] and not used[i]:
                    answer+=len(e)
                    used[i]=True
                    sucess=True
                    break
                else:all_p[i]=rotate(all_p[i])
            if sucess:break
    
    return answer