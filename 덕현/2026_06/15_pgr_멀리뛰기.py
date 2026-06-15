'''
프로그래머스 12914 멀리 뛰기

입력:
n

구조:
dp로 진행해서
1,2 넣고 두 개 더해서 뒤에꺼 만들고 마지막에 1234567 나눠서 반환
------------
파이썬은 나눗셈이 부동소수점이라 안된다해서 다른 방식으로 해ㅔ야한다고함
'''

import math

def solution(n):
    answer = 0

    for i in range(0, int(n / 2) + 1):
        one = n - (2 * i)
        two = i

        m = math.comb(one + two, two)

        answer += m
        answer = answer % 1234567

    return answer