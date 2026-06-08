'''
프로그래머스 87390 n^2 배열 자르기

입력:
n left right

구조:
전부 확인하고 1차원을 rc로하고 max값 구해서 +1하기
'''


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        r = i // n
        c = i % n

        if r > c:
            answer.append(r + 1)


        else:
            answer.append(c + 1)

    return answer