'''
프로그래머스 12987 숫자 게임

입력:
A B

구조:
B 순열해가지고 A랑 비교
최대 승점
--------------------
그리디로 푸는거라고 함
'''


def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    a = 0
    b = 0

    while a < len(A) and b < len(B):

        if B[b] > A[a]:

            answer += 1
            a += 1
            b += 1

        else:
            b += 1

    return answer