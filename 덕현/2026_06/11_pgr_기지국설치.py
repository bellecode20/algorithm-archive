'''
프로그래머스 12979 기지국 설치

입력:
n stations w

'''

def solution(n, stations, w):
    answer = 0
    now = 1
    size = w*2+1



    for station in stations:
        left = station-w
        right = station+w


        if now < left:
            cnt = left - now


            answer += cnt // size


            if cnt % size != 0:
                answer += 1


        now = right+1

    if now <= n:
        cnt = n-now+1

        answer += cnt//size

        if cnt % size!= 0:
            answer +=1

    return answer