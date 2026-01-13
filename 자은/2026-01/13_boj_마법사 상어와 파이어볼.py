dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def m_and_d(lst):

    M=S=D=0
    D_check=0
    for m,s,d in lst:
        M += m
        S += s
        if d%2 == 0:
            D_check+=1

    M = M//5

    if M == 0:  #질량이 0이 되면 해당 칸의 파이어볼 소멸
        lst=[]
        return lst
    
    S = S//len(lst)
    
    if D_check==len(lst) or D_check==0:
        lst=[]
        for i in range(0,8,2):
            lst.append((M,S,i))
    else:
        lst=[]
        for j in range(1,8,2):
            lst.append((M,S,j))
    
    return lst


N, M, K = map(int,input().split())
fireball_info = [list(map(int,input().split())) for _ in range(M)]

for _ in range(K):  #상어가 K번 명령
    arr = [[[] for _ in range(N)] for _ in range(N)]
    new_fireball_info=[]

    for r,c,m,s,d in fireball_info:
        nx = (r+dx[d]*s)%N
        ny = (c+dy[d]*s)%N
        arr[nx][ny].append((m,s,d))     #이동한 배열칸 위치에 파이어볼정보 담기
    
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue
            elif len(arr[i][j])==1:
                new_fireball_info.append([i,j,arr[i][j][0][0],arr[i][j][0][1],arr[i][j][0][2]])

            elif len(arr[i][j]) >= 2:     #해당 칸의 파이어볼 개수가 2개 이상일때
                arr[i][j]=m_and_d(arr[i][j])
                for lst in arr[i][j]:
                    new_fireball_info.append([i,j,lst[0],lst[1],lst[2]])
    fireball_info=new_fireball_info

result = 0

for lst in fireball_info:
    result+= lst[2]

print(result)



        

