def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    for i in range(N):
        while stack and stack[-1] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]

        stack.append(i)

    return answer