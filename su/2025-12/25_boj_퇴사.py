
# 테스트 케이스는 통과하지만
# 제출 시 히든케이스에는 실패하여
# 예외처리가 필요합니다. 

# 입력 텍스트 파일 실행 코드
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).parent
# sys.stdin = open(BASE_DIR / "input.txt", "r")
# input = sys.stdin.readline

N = int(input())
dp = [0] * N  # 
info = [[0, 0] for _ in range(N)]

for i in range(N):
    T, P = map(int, input().split())
    info[i] = [T, P]  # 기간, 금액


for i in range(N):
    if i + info[i][0] > N:  # i일에 상담시작해도 N일까지 끝이 안나는 경우
        dp[i] = 0
        continue

    for j in range(1, 6):
        if i-j  + info[i-j][0] - 1 >= i:  # i-j일 째에 시작한 상담이 i일째에도 끝이 안 난 경우 
           continue

        dp[i] = max(dp[i-j] +  info[i][1],  dp[i])


print(max(dp))