'''
프로그래머스 뒤에 있는 큰 수 찾기

입력:
numbers

구조:
앞부터 돌고 배열안에 아직 큰 수 못 찾은 위치 저장
값이 더 크면 채우기
끝까지 못 찾은 건 -1
'''
def solution(numbers):
    n = len(numbers)

    answer = [-1] * n
    stack = []

    for i in range(n):

        while stack:
            top = stack[-1]

            if numbers[top] < numbers[i]:
                answer[top] = numbers[i]
                stack.pop()
            else:
                break

        stack.append(i)

    return answer