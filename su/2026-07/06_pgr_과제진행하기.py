def get_minutes(start):
    h, m = map(int, start.split(":"))
    return h * 60 + m

def solution(plans):
    answer = []
    stack = []
    n = len(plans)

    plans.sort(key=lambda x: (x[1]))

    t = get_minutes(plans[0][1])  # 현재 시간
    stack.append((plans[0][0], int(plans[0][2])))  # 이름, 남은 시간
    i = 1

    while i < n:
        name, st, pt = plans[i]
        nxt_st = get_minutes(st)
        nxt_pt = int(pt)

        while stack and t < nxt_st:  # 붕 뜬 시간 동안 가능한 과제 처리
            gap = nxt_st - t 
            temp_name, temp_rest = stack.pop()

            if gap < temp_rest:  # 과제 처리하고도 과제 못 마친 경우
                stack.append((temp_name, temp_rest - gap))   
                break
            else:  # 이전 과제 완벽히 끝난 경우
                t += temp_rest
                answer.append(temp_name)

        t = nxt_st
        stack.append((name, nxt_pt))
        i += 1

    while stack:
        answer.append(stack.pop()[0])

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))