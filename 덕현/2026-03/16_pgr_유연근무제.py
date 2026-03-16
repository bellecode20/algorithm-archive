'''
프로그래머스 388351 유연근무제

입력:
schedules
timelogs
startday

구조:
직원마다 검사
희망 출근 시각 + 10분 계산
7일 돌면서 평일만 확인
하루라도 늦으면 실패
전부 통과하면 정답 +1
'''
def solution(schedules, timelogs, startday):

    n = len(schedules)
    ans = 0

    for i in range(n):

        t = schedules[i]
        h = t // 100
        m = t % 100

        m += 10
        if m >= 60:
            h += 1
            m -= 60

        limit = h * 100 + m

        ok = True
        day = startday

        for j in range(7):

            if day != 6 and day != 7:
                if timelogs[i][j] > limit:
                    ok = False
                    break

            day += 1
            if day == 8:
                day = 1

        if ok:
            ans += 1

    return ans