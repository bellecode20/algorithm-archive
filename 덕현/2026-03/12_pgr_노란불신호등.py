'''
프로그래머스 노란불 신호등

구조:
t를 1부터 증가
모든 신호등 상태 확인
전부 노란불이면 종료
'''
def solution(signals):

    t = 1

    while t <= 2000000:

        ok = True

        for g,y,r in signals:

            cycle = g + y + r
            cur = (t-1) % cycle

            if not (g <= cur < g+y):
                ok = False
                break

        if ok:
            return t

        t += 1

    return -1