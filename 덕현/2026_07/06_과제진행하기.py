'''
프로그래머스 176962 과제 진행하기

입력:
plans
'''

def change_time(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(plans):
    answer = []
    stack = []

    arr = []

    for plan in plans:
        name = plan[0]
        start = change_time(plan[1])
        playtime = int(plan[2])

        arr.append([name, start, playtime])

    arr.sort(key=lambda x: x[1])

    for i in range(len(arr) - 1):
        name = arr[i][0]
        start = arr[i][1]
        playtime = arr[i][2]

        next_start = arr[i + 1][1]

        gap = next_start - start

        if playtime <= gap:
            answer.append(name)
            gap -= playtime

            while stack and gap > 0:
                stop_name, stop_time = stack.pop()

                if stop_time <= gap:
                    answer.append(stop_name)
                    gap -= stop_time
                else:
                    stack.append([stop_name, stop_time - gap])
                    gap = 0

        else:
            stack.append([name, playtime - gap])

    answer.append(arr[-1][0])

    while stack:
        name, playtime = stack.pop()
        answer.append(name)

    return answer