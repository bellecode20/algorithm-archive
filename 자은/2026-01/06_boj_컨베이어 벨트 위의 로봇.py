N, K= map(int,input().split())
arr= list(map(int,input().split())) #각 칸의 내구도
robot=[0]*(2*N)
result=0

while True:
    result+=1   #몇번째 단계인지 세기

    #한칸씩 이동
    arr=arr[-1:]+arr[:-1]
    robot=robot[-1:]+robot[:-1]

    if robot[N-1]:  #N번째 칸에 도달한 로봇이 있다면 바로 내림
        robot[N-1]-=1
        
    for i in range(N-2,-1,-1):   #N-1번부터 0번칸 순서로 로봇들 이동
        if robot[i] and robot[i%(2*N)+1] ==0 and arr[i%(2*N)+1]>=1: #해당칸에 로봇이 있고/ 다음칸에 로봇이 없고/ 다음칸 내구도가 1 이상이면
            robot[i]-=1 #현재칸에서 로봇 빼고
            robot[i%(2*N)+1]+=1 #다음칸으로 로봇 이동
            arr[i%(2*N)+1]-=1   #내구도 1감소
    
    if robot[N-1]:  #N번째 칸에 도달한 로봇이 있다면 바로 내림
        robot[N-1]-=1

    if arr[0] > 0:  #올리는 위치의 내구도가 0보다 크면
        robot[0]+=1 #올리는 위치에 로봇올리고
        arr[0]-=1   #내구도 1감소

    cnt=arr.count(0)    #내구도가 0인 칸 개수세기

    if cnt>=K:
        break

print(result)
    