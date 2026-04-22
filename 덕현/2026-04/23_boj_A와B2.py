'''
BOJ 12919 A와 B2

입력:
S
T

구조:
DFS
줄여가면서 A면빼고 B면 뒤집기
길이 같음 가기
가능 1 아니면 0
'''

def dfs(n):
    global ans

    if ans == 1:
        return
    if len(n) == len(S):
        if n == S:
            ans = 1
        return
    if n[-1] == 'A':
        dfs(n[:-1])
    if n[0] == 'B':
        dfs(n[1:][::-1])



S = input()
T = input()


ans = 0
dfs(T)


print(ans)