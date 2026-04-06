'''
프로그래머스 155651 호텔 대실

입력:
book_time

구조:
시간 > 분
종료 시간 + 10
정렬하고
갱신 or 추가
방 개수 반환
'''
def solution(book_time):

    arr = []

    for i in range(len(book_time)):
        s = book_time[i][0]
        e = book_time[i][1]

        sh = int(s[0:2])
        sm = int(s[3:5])
        eh = int(e[0:2])
        em = int(e[3:5])

        start = sh * 60 + sm
        end = eh * 60 + em + 10

        arr.append((start, end))

    arr.sort()

    room = []

    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]

        idx = -1
        cur = float('inf')

        for j in range(len(room)):
            if room[j] <= start:
                if cur > room[j]:
                    cur = room[j]
                    idx = j

        if idx == -1:
            room.append(end)
        else:
            room[idx] = end

    return len(room)