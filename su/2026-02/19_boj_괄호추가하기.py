import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

N = int(input())
expression = input().strip()
answer = -int(1e9)

numbers = []
operators = []
for i, ch in enumerate(expression):
    if i % 2 == 0:
        numbers.append(int(ch))
    else:
        operators.append(ch)

def cal(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    

def dfs(idx, cur_val):
    global answer
    # 끝까지 도달하면
    if idx == len(operators):
        answer = max(answer, cur_val)
        return
    
    # 괄호 안 치기
    next_val = cal(cur_val, operators[idx], numbers[idx + 1])
    dfs(idx + 1, next_val)

    # 괄호 치는 경우
    if idx + 1 < len(operators):
        bracket_val = cal(numbers[idx + 1], operators[idx + 1], numbers[idx + 2])
        next_val = cal(cur_val, operators[idx], bracket_val)

        dfs(idx + 2, next_val)


dfs(0, numbers[0])

print(answer)