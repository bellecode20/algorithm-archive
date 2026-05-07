'''
프로그래머스 N으로 표현

입력:
N
number

구조:
DP라고 N 1~8쓴 경우 바로바로 만들어서 하기
set
'''

def solution(N, number):
    dp = []

    for i in range(9):
        dp.append(set())

    for i in range(1, 9):

        num = int(str(N) * i)
        dp[i].add(num)

        for j in range(1, i):

            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1