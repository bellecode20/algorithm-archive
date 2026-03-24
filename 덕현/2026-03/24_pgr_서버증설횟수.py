'''
프로그래머스 389479 서버 증설 횟수

입력:
players
m
k

구조:
시뮬
현재 시간에 살아있는 서버 수 관리
필요한 서버 수보다 부족하면 증설
증설한 서버는 k뒤 반납
전체 증설 횟수 누적해서 답
'''
def solution(players, m, k):

    ans = 0
    cnt = 0
    expire = [0] * (24 + k + 1)

    for i in range(24):

        cnt -= expire[i]

        need = players[i] // m

        if cnt < need:
            add = need - cnt
            ans += add
            cnt += add
            expire[i + k] += add

    return ans