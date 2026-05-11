'''
프로그래머스 롤케이크 자르기

입력:
topping

구조:
오른쪽에 다 넣고 왼쪽 옮기기
개수 줄이면서 왼 오 같으면 ++
'''


def solution(topping):
    right = {}
    left = set()
    answer = 0
    for x in topping:
        if x not in right:
            right[x] = 0
        right[x] += 1

    for x in topping:
        left.add(x)

        right[x] -= 1
        if right[x] == 0:
            del right[x]

        if len(left) == len(right):
            answer += 1

    return answer