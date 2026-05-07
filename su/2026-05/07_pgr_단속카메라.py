def solution(routes):
    answer = 0
    routes.sort()
    N = len(routes)
    time = -int(1e9)
    cnt = 0
    
    for i in range(N):
        s, e = routes[i]
        # 지금 범위가 커버 가능한 경우
        if time < s:  # 지금 범위가 커버 안되는 경우, 새로 카메라 넣기
            time = e
            cnt += 1
        else:  # 카메라 위치 재조정
            time = min(time, e)
            
    answer = cnt
    return answer