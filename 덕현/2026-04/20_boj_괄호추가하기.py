'''
BOJ 16637 괄호 추가하기

입력:
N
s

구조:
나누고 dfs
'''

def cal(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def dfs(idx, now):
    global ans

    if idx >= len(op):
        if now > ans:
            ans = now
        return

    a = cal(now, op[idx], num[idx + 1])
    dfs(idx + 1, a)

    if idx + 1 < len(op):
        b = cal(num[idx + 1], op[idx + 1], num[idx + 2])
        c = cal(now, op[idx], b)
        dfs(idx + 2, c)


N = int(input())
s = input()

num = []
op = []

for i in range(N):
    if i % 2 == 0:
        num.append(int(s[i]))
    else:
        op.append(s[i])

ans = -float('inf')
dfs(0, num[0])

print(ans)