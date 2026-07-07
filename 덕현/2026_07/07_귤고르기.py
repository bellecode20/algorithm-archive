'''
프로그래머스 138476 귤 고르기

입력:
k tangerine
'''

from collections import Counter

def solution(k, tangerine):
    answer = 0

    counter = Counter(tangerine)
    arr = list(counter.values())
    arr.sort(reverse=True)

    for cnt in arr:
        k -= cnt
        answer += 1

        if k <= 0:
            break

    return answer