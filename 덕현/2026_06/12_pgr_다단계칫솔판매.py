'''
프로그래머스 77486 다단계 칫솔 판매

입력:
enroll referral seller amount

구조:
이름별로 idx
answer 배열
판매자 > 추천인 돈 올리고 0원이면 stop
'''


def solution(enroll, referral, seller, amount):
    answer = []
    idx = {}

    for i in range(len(enroll)):
        answer.append(0)
        idx[enroll[i]] = i

    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100

        while name != '-':
            num = money // 10
            my_money = money - num

            cur = idx[name]
            answer[cur] += my_money

            if num == 0:
                break

            name = referral[cur]
            money = num

    return answer