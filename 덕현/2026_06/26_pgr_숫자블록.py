'''
프로그래머스 12923 숫자 블록

입력:
begin end

'''


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue

        ans = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i != 0:
                continue

            mok = num // i

            if mok <= 10000000:
                ans = mok
                break

            if i <= 10000000:
                ans = i

        answer.append(ans)

    return answer