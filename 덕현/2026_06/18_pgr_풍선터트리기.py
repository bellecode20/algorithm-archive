'''
프로그래머스 68646 풍선 터트리기

입력:
a

구조:
왼쪽 오른쪽 최솟값 하고?
'''


def solution(a):
    answer = 0
    n = len(a)
    left = [0] * n
    right = [0] * n

    left[0] = a[0]
    for i in range(1, n):

        if left[i - 1] < a[i]:

            left[i] = left[i - 1]

        else:
            left[i] = a[i]

    right[n - 1] = a[n - 1]

    for i in range(n - 2, -1, -1):

        if right[i + 1] < a[i]:
            right[i] = right[i + 1]


        else:
            right[i] = a[i]

    for i in range(n):

        if a[i] <= left[i] or a[i] <= right[i]:
            answer += 1

    return answer