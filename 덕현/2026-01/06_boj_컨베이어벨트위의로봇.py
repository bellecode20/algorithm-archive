'''
boj 20055 컨베이어 벨트 위의 로봇

입력:
N, K
A[2N] : 내구도 배열

구조:
1. 벨트 + 로봇 회전
2. 로봇 이동 (뒤에서 앞으로)
3. 로봇 올리기
4. 내구도 0의 개수 >= K 종료

- 로봇은 0 ~ N-1 위치만 관리
- N-1 위치 도착 시 즉시 제거
- 이동은 반드시 역순
'''
from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
robot = deque([False] * N)

step = 0

while True:
    step += 1

    A.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and A[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            A[i + 1] -= 1

    robot[-1] = False

    if not robot[0] and A[0] > 0:
        robot[0] = True
        A[0] -= 1

    if A.count(0) >= K:
        print(step)
        break
