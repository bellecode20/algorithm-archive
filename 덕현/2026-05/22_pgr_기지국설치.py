'''
프로그래머스 12979 기지국 설치

입력:
n stations w

구조:
answer = 0 now = 1
빈 구간만 생각해서 이어지게 다음으로 넘기기
'''

def solution(n, stations, w):
    answer = 0
    now = 1
    size = 2 * w + 1


    for station in stations:
        left = station - w
        right = station + w
        if now < left:
            cnt = left - now
            answer += cnt // size
            if cnt % size != 0:
                answer += 1



        now = right + 1


    if now <= n:
        cnt = n - now + 1

        answer += cnt // size
        if cnt % size != 0:
            answer += 1

    return answer