'''
프로그래머스 388352 비밀 코드 해독

입력:
n
q
ans

구조:
1부터 n까지에서 5개 조합 완전탐색
각 조합마다 질문들과 겹치는 개수 확인
응답값과 전부 같으면 정답 +1
'''
from itertools import combinations

def solution(n, q, ans):

    answer = 0

    for pick in combinations(range(1, n+1), 5):

        ok = True

        for i in range(len(q)):

            cnt = 0

            for j in range(5):
                if q[i][j] in pick:
                    cnt += 1

            if cnt != ans[i]:
                ok = False
                break

        if ok:
            answer += 1

    return answer