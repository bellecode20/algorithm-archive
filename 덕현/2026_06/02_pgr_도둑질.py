'''
프로그래머스 42897 도둑질

입력:
money

구조:
DP라고 함
첫 집 터는 경우와 아닌 경우만 계산해서 갱신하기?
둘중에 큰값
'''

def solution(money):
    n = len(money)

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = money[0]
    dp1[1] = money[0]

    for i in range(2, n-1):
        num1 = dp1[i -1]
        num2 = dp1[i- 2] + money[i]

        if num1 > num2:
            dp1[i] = num1
        else:
            dp1[i] = num2

    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        num1 = dp2[i-1]
        num2 = dp2[i -2] + money[i]

        if num1 > num2:
            dp2[i] = num1
        else:
            dp2[i] = num2

    if dp1[n - 2] > dp2[n -1]:
        return dp1[n -2]

    return dp2[n -1]