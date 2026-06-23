'''
프로그래머스 131704 택배상자

입력:
order

구조:
stack으로 했던거
'''


def solution(order):
    answer = 0
    stack = []

    for i in range(1, len(order) + 1):

        stack.append(i)

        while stack:
            now = stack[-1]

            if now == order[answer]:
                stack.pop()
                answer += 1


            else:
                breaka

            if answer == len(order):
                break

    return answer