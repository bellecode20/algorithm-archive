# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

'''
수정이 필요한 코드입니다

dfs로 진행하고 dp로 연산값들을 저장해 두는 방식으로 계획 중
남은 연산자들을 어떤 자료구조료 표현할지 더 고민이 필요할 듯 하다
'''

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))  # + - x //
INF = float('inf')
dp = defaultdict(int)
maximum, minimum = 0, INF

def dfs(depth, rest):  
    if depth == N:
        maximum = max(maximum, dp[(depth, rest)])
        minimum = min(minimum, dp[(depth, rest)])
    
    for i in range(4):
        if operators[i] == 0:
            continue

        if depth == 0:
            next_rest = rest[:]
            next_rest[i] -= 1

            if i == 0:
                next_value = A[0] + A[1]
            elif i == 1:
                next_value = A[0] - A[1]
            elif i == 2:
                next_value = A[0] * A[1]
            else:
                next_value = A[0] // A[1]


            dp[(depth + 1, next_rest)] = next_value
            dfs(depth + 1, next_rest)
            continue


        else:
            if i == 0:
                next_value = dp[(depth, rest)] + A[depth + 1]
            elif i == 1:
                next_value = dp[(depth, rest)] - A[depth + 1]
            elif i == 2:
                next_value = dp[(depth, rest)] * A[depth + 1]
            else:
                next_value = dp[(depth, rest)] // A[depth + 1]

            next_rest[i] -= 1
            dp[(depth + 1, next_rest)] = next_value
            dfs(depth + 1, next_rest)


for i in range(4):
    if operators[i] > 0:
        rest_nums = operators[:]
        rest_nums[i] -= 1
        dfs(0, rest_nums)

print(maximum)
print(minimum)
# 5 6 7
# 0 0 1 1

# A[0] = 5
# A[1] = 6

# dfs(0):
#     depth == 0이면
#     A[0] * A[1]

#     5 * 6 (0 * 1)

# dfs(1)
#     기존 꺼 에다가 A[i + 1]