'''
프로그래머스 389481 봉인된 주문

입력:
n bans
'''


def make_num(word):
    num = 0

    for ch in word:
        num *= 26
        num += ord(ch) - ord('a') + 1

    return num


def make_word(num):
    answer = ''

    while num > 0:
        num -= 1
        ch = chr(num % 26 + ord('a'))
        answer = ch + answer
        num //= 26

    return answer


def solution(n, bans):
    arr = []

    for ban in bans:
        arr.append(make_num(ban))
    arr.sort()

    for num in arr:
        if num <= n:
            n += 1
        else:
            break
    answer = make_word(n)

    return answer