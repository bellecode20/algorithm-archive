'''
프로그래머스 기능개발

입력:
progresses
speeds

구조:
끝나는 날짜 묶기 더 오래걸리면 컷
묶인 개수 answer에 넣기
'''

def solution(progresses, speeds):
    days = []

    for i in range(len(progresses)):
        left = 100 - progresses[i]

        if left % speeds[i] == 0:
            day = left // speeds[i]
        else:
            day = left // speeds[i] + 1

        days.append(day)

    answer = []

    cur = days[0]
    cnt = 1

    for i in range(1, len(days)):
        if days[i] <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cur = days[i]
            cnt = 1

    answer.append(cnt)

    return answer