'''
BOJ 6603 로또

입력:
temp
graph

구조:
조합으로 dfs하면될듯?
'''

def dfs(idx, cnt):
    if cnt == 6:
        for i in range(6):
            print(pick[i], end=' ')
        print()
        return

    for i in range(idx, k):
        pick.append(graph[i])
        dfs(i + 1, cnt + 1)
        pick.pop()


while 1:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break

    k = temp[0]
    graph = temp[1:]

    pick = []
    dfs(0, 0)
    print()
