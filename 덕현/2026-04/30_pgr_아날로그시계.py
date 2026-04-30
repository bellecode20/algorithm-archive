'''
프로그래머스 아날로그 시계

입력:
h1 m1 s1 h2 m2 s2

구조:
시간별로 알람 개수 세기
초분, 초시 겹침
0,12는 1번만
'''

def get_cnt(t):
    a = (59 * t) // 3600 + 1
    b = (719 * t) // 43200 + 1
    same = t // 43200 + 1

    return a + b - same


def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    ans = get_cnt(end) - get_cnt(start)

    if (59 * start) % 3600 == 0 or (719 * start) % 43200 == 0:
        ans += 1

    return ans