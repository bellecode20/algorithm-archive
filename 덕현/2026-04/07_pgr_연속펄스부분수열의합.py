'''
프로그래머스 161988 연속펄스 부분수열의 합

입력:
sequence

구조:
부호 번갈아 곱
최대합
최소합
둘 중 큰 값 반환
'''


def solution(sequence):
    arr = []
    sign = 1

    for i in range(len(sequence)):
        arr.append(sequence[i] * sign)
        sign *= -1

    max_dp = arr[0]
    min_dp = arr[0]
    ans = arr[0]

    for i in range(1, len(arr)):
        if max_dp + arr[i] > arr[i]:
            max_dp = max_dp + arr[i]
        else:
            max_dp = arr[i]

        if min_dp + arr[i] < arr[i]:
            min_dp = min_dp + arr[i]
        else:
            min_dp = arr[i]

        if ans < max_dp:
            ans = max_dp
        if ans < -min_dp:
            ans = -min_dp

    return ans