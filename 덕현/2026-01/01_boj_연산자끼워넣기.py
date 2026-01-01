'''
연산자 끼원허기

연산자는 각 들어갈 부분이 정해져 있으니까 전부 조합을 짜는거보단 하고 돌아가는 방식이 시간을 덜 먹었던거같은데

입력 :
N
numbers
ops

'''

def dfs(cnt, total):
    global max_val, min_val
    if cnt == N - 1:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            if i == 0:
                dfs(cnt + 1, total + numbers[cnt + 1])
            elif i == 1:
                dfs(cnt + 1, total - numbers[cnt + 1])
            elif i == 2:
                dfs(cnt + 1, total * numbers[cnt + 1])
            elif i == 3:
                if total < 0:
                    dfs(cnt + 1, -(-total // numbers[cnt + 1]))
                else:
                    dfs(cnt + 1, total // numbers[cnt + 1])
            ops[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

dfs(0, numbers[0])
print(max_val)
print(min_val)