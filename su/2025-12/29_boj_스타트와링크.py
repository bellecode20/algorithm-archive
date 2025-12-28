# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = float('INF')

scores = [[0] * N for _ in range(N)]
numbers = set([i for i in range(N)])

def calc(selected):
    temp = 0
    for r in selected:
        for c in selected:
            if r == c:
                continue
            temp += graph[r][c]

    return temp


def dfs(selected, idx):
    global answer

    if len(selected) == N // 2:
        start, link = calc(selected), calc(list(numbers - set(selected)))
        answer = min(answer, abs(start - link))
    
    for j in range(idx, N):
        dfs(selected + [j], j + 1)

dfs([0], 1)  # 0번째 숫자를 들어간 팀을 항상 스타트팀이라고 생각해서 대칭을 줄인다. (0,1이 스타트팀이고 2,3이 링크팀 경우 == 2, 3이 스타트팀, 0,1이 링크팀이 아닌 경우엔 점수가 같음. 이 중복 케이스 제외하기 위함)
print(answer)