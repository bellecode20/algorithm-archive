def solution(players, m, k):
    answer = 0

    for i in range(len(players)):
        if players[i]<m:
            continue
        need=players[i]//m  #증설된 서버개수
        answer+=need
        for j in range(k):  #서버 수명만큼 미리 인원수 빼기
            if i+j<24:
                players[i+j] -= need*m
                
    return answer