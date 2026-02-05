'''

조합으로 고를 때 연속된 열은 뽑을 수 없음

[사다리 이동 로직]
1열부터 N열까지
1. (0,1),(0,2),(0,3)...각 세로줄마다 0번째 행에서 출발
2. 똑같은 열 +1행으로 이동
3. -1열(왼쪽)과 +1열(오른쪽)을 확인해서 연결 여부 확인
4. 연결된 쪽으로 이동. 연결 되어 있지 않으면 제자리.
5. 다음 행으로 이동
위를 반복


'''
from itertools import combinations
from copy import deepcopy

def go(start_col):
    curr_c = start_col
    for r in range(1, H + 1):
        if isConnected[r][curr_c]:       # 오른쪽 이동
            curr_c += 1
        elif curr_c > 1 and isConnected[r][curr_c - 1]: # 왼쪽 이동
            curr_c -= 1
    return curr_c == start_col # 시작 열과 끝 열이 같은지 바로 반환
        

def is_valid(combs):
    for r, c in combs:
            if isConnected[r][c]: return False
            if c > 1 and isConnected[r][c-1]: return False
            if c < N-1 and isConnected[r][c+1]: return False
    for i in range(len(combs)-1):
        for j in range(i+1,len(combs)):
            r1,c1=combs[i]
            r2,c2=combs[j]
            if r1==r2 and abs(c1-c2)==1:
                return False
    return True

N, M, H=map(int,input().split())
width_lines=[list(map(int,input().split())) for _ in range(M)]
isConnected=[[False]*(N+1) for _ in range(H+1)]
combs=[(r, c) for r in range(1,H+1) for c in range(1,N)]
result=-1
finish=False
if M>0:
    for a,b in width_lines:isConnected[a][b]=True
if M==0:print(0)
else:
    for t in range(1,4):
        
        if t==1:
            for r,c in combs:
                if isConnected[r][c]:continue
                if (c > 1 and isConnected[r][c-1]) or (c < N-1 and isConnected[r][c+1]):continue
                success=True
                isConnected[r][c]=True
                for n in range(1,N+1):
                    if not go(n):   #열 하나라도 실패하면
                        success=False
                        break   #해당 조합 종료
                isConnected[r][c]=False
                if success:
                    result=1
                    finish=True
                    break    #성공했다면 종료
        else:
            all_combs=combinations(combs,t)
            valid_combs=[]
            for c in all_combs:
                if is_valid(c):valid_combs.append(c)
            for comb in valid_combs:   #각 조합마다 사다리조작 시작
                success=True
                for r,c in comb:isConnected[r][c]=True
                for n in range(1,N+1):
                    if not go(n):   #열 하나라도 실패하면 해당 조합 종료
                        success=False
                        break
                for r,c in comb:isConnected[r][c]=False
                if success:
                    result=t
                    finish=True
                    break    #성공했다면 종료
        if finish:break
    print(result)