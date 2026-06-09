'''
프로그래머스 12971 스티커 모으기(2)

입력:
sticker

구조:
dp라고 하고
스티커가 1개인 경우랑 첫번째 뗴는거랑 계산하고 첫번째 안 때는거 계산해서 나눠서계산
'''


def solution(sticker):
    n = len(sticker)

    if n == 1:
        return sticker[0]

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]

    for i in range(2, n - 1):
        num1 = dp1[i - 1]
        num2 = dp1[i - 2] + sticker[i]

        if num1 > num2:
            dp1[i] = num1


        else:
            dp1[i] = num2

    dp2[0] = 0

    dp2[1] = sticker[1]

    for i in range(2, n):
        num1 = dp2[i - 1]
        num2 = dp2[i - 2] + sticker[i]

        if num1 > num2:
            dp2[i] = num1


        else:
            dp2[i] = num2

    if dp1[n - 2] > dp2[n - 1]:
        return dp1[n - 2]

    return dp2[n - 1]