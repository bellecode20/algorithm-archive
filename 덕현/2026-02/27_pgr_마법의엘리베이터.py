'''
프로그래머스 148653 마법의 엘리베이터

입력:
storey

구조:
1의 자리부터 시작해서
자리수가 0~4면 down 후 0만들기
자리수가 6~9면 올려가지고 10 만들고 다음 자리에 +1 넘기기
자리수가 5면 다음 자리 보고 결정하는데,
다음 자리가 5 이상이면 올림, 아니면 내림
'''

def solution(storey):
    ans = 0

    while storey > 0:
        cur = storey % 10
        nxt = (storey // 10) % 10

        if cur < 5:
            ans += cur
            storey -= cur
        elif cur > 5:
            ans += 10 - cur
            storey += 10 - cur
        else:
            if nxt >= 5:
                ans += 5
                storey += 5
            else:
                ans += 5
                storey -= 5

        storey //= 10

    return ans