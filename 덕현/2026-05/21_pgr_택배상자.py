'''
프로그래머스 131704 택배상자

입력:
order

구조:
stack으로해서 answer+1
'''

def solution(order):
    answer = 0
    stack = []

    for num in range(1, len(order) + 1):
        stack.append(num)

        while stack:
            top = stack[-1]

            if top == order[answer]:
                stack.pop()
                answer += 1
            else:
                break

            if answer == len(order):
                break

    return answer