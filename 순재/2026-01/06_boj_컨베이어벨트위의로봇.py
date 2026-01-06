from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * (2 * n))
step = 0

zero_cnt = belt.count(0)

while zero_cnt < k:
    step += 1

    belt.rotate(1)
    robot.rotate(1)

    if robot[n-1] == 1:
        robot[n-1] = 0

    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                zero_cnt += 1

    if robot[n-1] == 1:
        robot[n-1] = 0

    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            zero_cnt += 1

print(step)