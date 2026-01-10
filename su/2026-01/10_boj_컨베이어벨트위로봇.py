# https://www.acmicpc.net/problem/20055

from collections import deque
N, K = map(int, input().split())  # N, 종료 카운트

belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
answer = 0

turn = 1
while True:
    # 1. 벨트가 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)

    if robot[N-1] != 0:
        robot[N-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 이동할 수 있다면 이동하기
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1], robot[i] = robot[i], robot[i+1]
            belt[i+1] -= 1
    
    if robot[N-1] != 0:
        robot[N-1] = 0

    # 3. 내구도가 d이 아니라면 올리는 위치에 로봇을 올린다.
    if belt[0] != 0 and robot[0] == 0:
        belt[0] -= 1
        robot[0] = 1

    zero_cnt = sum(1 for b in belt if b == 0)
    if zero_cnt >= K:
        answer = turn
        break

    turn += 1

print(answer)