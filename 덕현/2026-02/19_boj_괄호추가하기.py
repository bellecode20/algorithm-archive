'''
BOJ 16637 괄호 추가하기

입력:
N
exp

구조:
연산자 기준으로 괄호 넣을지 말지? dfs?
겹치면 안됨..
최대값 갱신
'''

def calc(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return a * b

def dfs(i, cur):
    global ans

    if i == len(ops):
        if cur > ans:
            ans = cur
        return

    n = calc(cur, ops[i], nums[i + 1])
    dfs(i + 1, n)

    if i + 1 < len(ops):
        inside = calc(nums[i + 1], ops[i + 1], nums[i + 2])
        n2 = calc(cur, ops[i], inside)
        dfs(i + 2, n2)


N = int(input())
exp = input()

nums = []
ops = []

for i in range(N):
    if i % 2 == 0:
        nums.append(int(exp[i]))
    else:
        ops.append(exp[i])

ans = float('-inf')

dfs(0, nums[0])

print(ans)
