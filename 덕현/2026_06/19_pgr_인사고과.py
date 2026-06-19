'''
프로그래머스 152995 인사고과

입력:
scores




'''


def solution(scores):
    answer = 1
    wan_a = scores[0][0]
    wan_b = scores[0][1]
    wan_sum = wan_a + wan_b

    scores.sort(key=lambda x: (-x[0], x[1]))

    max_b = 0

    for score in scores:
        a = score[0]
        b = score[1]

        if b < max_b:

            if a == wan_a and b == wan_b:
                return -1
            continue

        if b > max_b:
            max_b = b

        if a + b > wan_sum:
            answer += 1

    return answer