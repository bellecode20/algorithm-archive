def right_turn(lst):
    lst=lst[-1]+lst[:-1]
    return lst

def left_turn(lst):
    lst=lst[1:]+lst[0]
    return lst

arr=[input() for _ in range(4)]
K=int(input())  #회전횟수
sum=0
for _ in range(K):
    wheel_num, direction=map(int,input().split())
    wheel_num-=1

    right=set()
    left=set()

    num=wheel_num
    dr=direction
    while num<3:    #해당 톱니바퀴의 오른쪽 톱니바퀴 확인
            
        if arr[num][2]!=arr[num+1][6]:  #맞닿은 극이 다를때
            if dr==-1:   #시계방향이면
                right.add(num+1)
                dr=1
            else:
                left.add(num+1)
                dr=-1
            num+=1
        else:
            break

    num=wheel_num
    dr=direction
    while num>=1:   #해당 톱니바퀴의 왼쪽 톱니바퀴 확인
        if arr[num][6]!=arr[num-1][2]:
            if dr==-1:
                right.add(num-1)
                dr=1
            else:
                left.add(num-1)
                dr=-1
            num-=1
        else:
            break

    if direction==1:
        right.add(wheel_num)
    else:
        left.add(wheel_num)

    #회전
    for r in right:
        arr[r]=right_turn(arr[r])
    for l in left:
        arr[l]=left_turn(arr[l])

for i in range(4):
    if arr[i][0]=='1':
        sum+=(2**i)
print(sum)
    