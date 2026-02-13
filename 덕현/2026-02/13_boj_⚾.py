'''
BOJ 17281 ⚾

입력:
N
graph

구조:
순열?
1번 선수는 4번 타자로 고정
나머지 8명 순서를 전부 만들기?
시뮬 돌려서 점수 계산
최대 점수 갱신하기
'''
from itertools import permutations

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

players = [1,2,3,4,5,6,7,8]
ans = 0

for perm in permutations(players):
    order = [0] * 9
    order[3] = 0

    idx = 0
    for i in range(9):
        if i == 3:
            continue


        order[i] = perm[idx]
        idx += 1

    score = 0
    cur = 0

    for j in range(N):

        out = 0
        b1 = b2 = b3 = 0

        while out < 3:
            p = order[cur]
            cur = (cur + 1) % 9

            res = graph[j][p]

            if res == 0:
                out += 1


            elif res == 1:
                score += b3
                b3 = b2
                b2 = b1
                b1 = 1



            elif res == 2:
                score += b3 + b2
                b3 = b1
                b2 = 1
                b1 = 0



            elif res == 3:
                score += b3 + b2 + b1
                b3 = 1
                b2 = 0
                b1 = 0


            else:
                score += b3 + b2 + b1 + 1
                b1 = b2 = b3 = 0

    if score > ans:
        ans = score

print(ans)
