def solution(board):
    answer = 1
    cnt_o=cnt_x=0
    obingo=False
    xbingo=False
    for i in range(3):
        #행이 같은지
        if board[i].count('O')==3:obingo=True
        if board[i].count('X')==3:xbingo=True
        
        #열이 같은지
        if board[0][i]=='O':
            if (board[0][i]==board[1][i] and board[1][i]==board[2][i]):
                obingo=True
        elif board[0][i]=='X':
            if (board[0][i]==board[1][i] and board[1][i]==board[2][i]):
                xbingo=True
                
        cnt_o+=board[i].count('O')
        cnt_x+=board[i].count('X')
        
        
    #대각선이 같은지 
    if board[0][0]=='O'and (board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        obingo=True
    if board[0][2]=='O' and(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        obingo=True
    if board[0][0]=='X'and (board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        xbingo=True
    if board[0][2]=='X' and(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        xbingo=True
    

    #X(후공)가 O(선공)보다 많을때, 둘다 빙고, 차이가 1보다 클때, x가 빙고인데 개수가 같지 않을때, o가 빙고인데 개수차이가 1이 아닐때
    if (cnt_x>cnt_o) or (obingo and xbingo) or (cnt_o-cnt_x)>1 or (xbingo and cnt_x!=cnt_o) or (obingo and (cnt_o-cnt_x)!=1):
        answer=0
    return answer