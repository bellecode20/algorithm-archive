'''
입력:
r, c, k = map(int, input().split())(A[r][c] = k가 되는 수)
무조건 3 by 3 행렬이므로
graph = for i in range(3):
            for j in range(3):

로직:
1. 행의 개수와 열의 개수를 판단
    - 정렬 수행 ( 출현 빈도 수가 적은 순서대로 정렬 )
    - 수를 받을 때, 어떤 수가 몇 개 있는지에 대해서 받아야 하는걸 어떻게 할건지
    - 그 수를 받고 개수를 기준으로 오름차순 정렬하기 ( 람다? )
    - 배열이 실시간으로 가변적인 상태가 될텐데 가변적인 상태를 계속 유지 해야 하는가? (고정으로 해야하는가?)
'''

r, c, k = map(int,input().split())
r -= 1
c -= 1

graph = [[0]*3 for _ in range(3)]


for i in range(3):
    x,y,z = map(int,input().split())
    graph[i][0] = x
    graph[i][1] = y
    graph[i][2] = z

t = 0
while t <= 100:
    if 0<= r < len(graph) and 0 <= c < len(graph[0]) and graph[r][c] == k:
        print(t)
        break

    if len(graph) >= len(graph[0]):
        new_graph = []
        max_len = 0

        for row in graph:
            save = {}
            for x in row:
                if x == 0:
                    continue
                save[x] = save.get(x, 0) + 1

            sort_result = sorted(save.items(), key=lambda x: (x[1], x[0]))

            new_row = []
            for num, cnt in sort_result:
                new_row.append(num)
                new_row.append(cnt)

            if len(new_row) > 100:
                new_row = new_row[:100]

            max_len = max(max_len, len(new_row))
            new_graph.append(new_row)

        max_len = min(max_len, 100)
        for row in new_graph:
            row += [0] * (max_len - len(row))

        graph = new_graph

    else:
        trans = list(map(list, zip(*graph)))
        new_trans = []
        max_len = 0

        for row in trans:
            save = {}
            for x in row:
                if x == 0:
                    continue
                save[x] = save.get(x, 0) + 1

            sort_result = sorted(save.items(), key=lambda x: (x[1], x[0]))

            new_row = []
            for num, cnt in sort_result:
                new_row.append(num)
                new_row.append(cnt)

            if len(new_row) > 100:
                new_row = new_row[:100]

            max_len = max(max_len, len(new_row))
            new_trans.append(new_row)

        max_len = min(max_len, 100)
        for row in new_trans:
            row += [0] * (max_len - len(row))

        graph = list(map(list, zip(*new_trans)))

    t += 1
else:
    print(-1)