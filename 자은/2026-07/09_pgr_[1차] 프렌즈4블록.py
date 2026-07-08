dx=[0,1,1]  # → ↘ ↓
dy=[1,1,0]

def solution(m, n, board):
    answer = 0
    board=[list(lst)for lst in board]
    
    def is_boom(x,y):
        nonlocal boom
        for i in range(3):
            nx,ny=x+dx[i],y+dy[i]
            if board[nx][ny]!=board[x][y]:
                return False
        return True
    
    while True:
        game_over=True
        
        #터뜨려야하는 블록 찾기
        boom=set()
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] != '.' and is_boom(r,c):
                    boom.update([(r,c),(r,c+1),(r+1,c+1),(r+1,c)])
                    game_over=False
            
        if not game_over:
            #블록 터뜨리기
            for x,y in boom:board[x][y]='.'
            #블록 떨어지기
            for c in range(n):
                for r in range(m-1,0,-1):
                    if board[r][c]=='.':
                        nx=r
                        while nx>0 and board[nx][c]=='.':nx-=1
                        if nx==0 and board[nx][c]=='.':break
                        board[r][c]=board[nx][c]
                        board[nx][c]='.'
        else: break
            
    for lst in board:answer+=lst.count('.')
            
    return answer