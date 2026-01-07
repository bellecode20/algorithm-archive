'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.

2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.

3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로

4. 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

===========

학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다. 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.

'''

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def satisfaction_check(x,y):
    student_number=arr[x][y]
    like_cnt=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if arr[nx][ny] in like_info[student_number]:
            like_cnt+=1
    if like_cnt==0:
        return 0
    else:
        return 10**(like_cnt-1)
    
# def set_seat(n,likes):
#     like_max=-1
#     final_x=0
#     final_y=0
#     empty=-1
    
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:  #빈자리일때만
#                 like_cnt=0
#                 empty_cnt=0
#                 for k in range(4):
#                     nx=i+dx[k]
#                     ny=j+dy[k]

#                     if nx<0 or nx>=N or ny<0 or ny>=N:
#                         continue
#                     if arr[nx][ny] in likes:
#                         like_cnt+=1
#                     if arr[nx][ny]==0:
#                         empty_cnt+=1

#                 if like_cnt>like_max:   #좋아하는애가 제일 많은 자리가 많을때
#                     final_x, final_y, empty= i,j,empty_cnt
#                 elif like_cnt==like_max:    #인접한칸에 좋아하는애 수가 같다면
#                     if empty_cnt>empty:     #빈자리가 더 많을때
#                         final_x, final_y, empty= i,j,empty_cnt

#     arr[final_x][final_y]=n

#     return

def set_seat(n, likes):
    candidates = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0: continue # 빈칸 아니면 패스
            
            like_cnt = 0
            empty_cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] in likes:
                        like_cnt += 1
                    if arr[nx][ny] == 0:
                        empty_cnt += 1
            
            # 정렬할 때 행/열은 작은 게 앞으로 오게 해야함
            candidates.append((like_cnt, empty_cnt, -i, -j))

    candidates.sort(reverse=True)
    best_x, best_y = candidates[0][2],candidates[0][3]
    arr[-best_x][-best_y] = n


N=int(input())
like_info = [[] for _ in range(N*N + 1)]
arr=[[0]*N for _ in range(N)]
result=0

for _ in range(N*N):

    student_number,*likes=map(int,input().split())
    like_info[student_number] = likes
    set_seat(student_number,likes)

for i in range(N):
    for j in range(N):
        result+=satisfaction_check(i,j)
print(result)