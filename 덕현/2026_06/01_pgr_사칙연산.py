'''
프로그래머스 1843 사칙연산

입력:
arr

구조:
DP라고 함
양수 음수에 나눠서 더하고 빼기
'''

def solution(arr):
    n = len(arr) // 2 + 1

    max_dp = []
    min_dp = []

    for i in range(n):
        max_dp.append([float('-inf')] * n)
        min_dp.append([float('inf')] * n)

    for i in range(n):
        num = int(arr[i * 2])
        max_dp[i][i] = num
        min_dp[i][i] = num

    for cnt in range(2, n + 1):
        for i in range(n):
            j = i + cnt - 1

            if j >= n:
                break

            for k in range(i, j):
                op = arr[k*2+1]

                if op == '+':
                    num = max_dp[i][k] + max_dp[k+1][j]
                    if num > max_dp[i][j]:
                        max_dp[i][j] = num

                    num = min_dp[i][k] + min_dp[k+1][j]
                    if num < min_dp[i][j]:
                        min_dp[i][j] = num

                else:
                    num = max_dp[i][k] - min_dp[k+1][j]
                    if num > max_dp[i][j]:
                        max_dp[i][j] = num

                    num = min_dp[i][k] - max_dp[k+1][j]
                    if num < min_dp[i][j]:
                        min_dp[i][j] = num

    return max_dp[0][n - 1]