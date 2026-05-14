'''
프로그래머스 42584 주식가격

입력:
prices

구조:
for
    for
가격 마다 뒤 확인해서 cnt + 1
떨어지면 answer.append(cnt)
'''

def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0

        for j in range(i + 1, len(prices)):
            cnt += 1

            if prices[i] > prices[j]:
                break

        answer.append(cnt)

    return answer