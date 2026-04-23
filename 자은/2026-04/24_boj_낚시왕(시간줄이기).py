def update():
    temp=[]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:   #해당 칸에 상어가 있다면
                s,d,z=arr[i][j]
                temp.append([i,j,s,d,z])
    return temp

dx=[-1,1,0,0]   #위,아래,오른쪽,왼쪽
dy=[0,0,1,-1]

R,C,M=map(int,input().split())
infos=[list(map(int,input().split())) for _ in range(M)] #행,열,속력,방향,크기
ans=0

for i in range(len(infos)):
    infos[i][0]-=1
    infos[i][1]-=1
    infos[i][3]-=1

for t in range(C):  #열의 크기만큼(=낚시꾼이 이동하는 만큼)
    catch=R
    catch_idx=-1
    for i in range(len(infos)):
        if infos[i][1]==t and infos[i][0]<catch:  #낚시왕이 있는 열에서 가장 가까운 상어라면
            catch=infos[i][0]
            catch_idx=i

    if catch != R:  #낚시꾼이 있는 열에 상어가 있었다면
        ans+=infos[catch_idx][4]    #잡은 상어 크기만큼
        del infos[catch_idx]    #상어잡기(=해당 상어 삭제)

    arr=[[False]*C for _ in range(R)]    #속력,방향,크기 저장

    for i in range(len(infos)):
        r,c,s,d,z=infos[i]

        if d in (0, 1):  # 위아래 이동
            period = 2 * (R - 1)
            if R == 1:period = 1
            turn = s % period
        else:            # 좌우 이동
            period = 2 * (C - 1)
            if C == 1:period = 1
            turn = s % period

        while turn>0:
            nx,ny=r+dx[d],c+dy[d]
            if nx<0 or nx>=R or ny<0 or ny>=C:  #가려는 곳이 격자를 벗어나면
                d=d^1   #방향 반대로 바꾸기
                nx,ny=r+dx[d],c+dy[d]
            r,c=nx,ny
            turn-=1

        move=True
        if arr[r][c]:   #해당 칸에 이미 다른 상어가 있을때
            if z<arr[r][c][2]:  #그 상어가 크기가 더 크다면
                move=False
        if move:
            arr[r][c]=(s,d,z)
        
    infos=update()  #상어정보 업데이트
print(ans)