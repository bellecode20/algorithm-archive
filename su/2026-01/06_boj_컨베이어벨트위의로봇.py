import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 수정 필요한 코드
# 회전할 때 belt와 robot을 같이 돌리고
# 로봇 이동 방향도 수정 필요

N, K = map(int, input().split())  # N, 종료 카운트

belt = list(map(int, input().split()))
robot = [0] * (2 * N)
answer = 0

# 인덱스 밀기
turn = 1
while True:
    new_belt = [0] * (2 * N)
    new_robot = [0] * (2 * N)

    # 벨트 회전
    for i in range(N * 2):
        new_belt[i] = belt[i-1]  # 내구도
    
    # 이동하기
    cnt = 0
    is_end = False
    for i in range(N * 2):
        print(f"{i}===========")
        print(belt)
        if is_end:
            break
        # 로봇 회전
        if robot[i] == 0 and robot[i - 1] == 1 and new_belt[i] >= 1:  # 옮기려는 위치에 로봇이 없고, 내구도가 1이상인 경우 이동한다.
            new_robot[i] = robot[i-1]
            new_belt[i] -= 1
            if new_belt[i] == 0:
                cnt += 1
            if i == N - 1 and new_robot[i] == 1:
                new_robot[i] = 0
        
        # 올리는 위치에 로봇을 올리기
        if new_belt[0] > 0 and new_robot[0] == 0:
            new_robot[0] = 1
            new_belt[0] -= 1
            if new_belt[i] == 0:
                cnt += 1 

        # 내구도 점검, 종료
        if cnt >= K:
            is_end = True
            break

    turn += 1
print(answer)