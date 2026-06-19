'''
O(n)으로 풀어야 함

'''


def solution(scores):  # 완호의 총점보다 높은 사람 수만 세는 풀이
    wanho_a, wanho_b = scores[0]
    wanho_total = wanho_a + wanho_b

    scores.sort(key=lambda x: (-x[0], x[1]))

    max_peer = -1
    rank = 1

    for attitude, peer in scores:
        # 앞에서 나온 사람 중 동료 평가 점수가 더 높은 사람이 존재
        if peer < max_peer:
            # 완호가 인센티브 제외 대상
            if attitude == wanho_a and peer == wanho_b:
                return -1

            continue

        max_peer = max(max_peer, peer)

        # 인센티브 대상자 중 완호보다 합이 큰 사람
        if attitude + peer > wanho_total:
            rank += 1

    return rank


# 실제로 후보자 목록 만들고 순서 세는 풀이
def solution_2(scores):
    n = len(scores)
    for i in range(n):
        scores[i].append(i + 1)
        
    scores.sort(key= lambda x: (-x[0], x[1]))  # 근태 높은 순, 동평 낮은 순서대로 정렬 되어있음. 즉, 뒤에있는 애는 앞에 있는 애때문에 떨어질 일이 없다
    
    max_peer = scores[0][1]
    candidates = [(scores[0][0] + scores[0][1], scores[0][2])]
    
    for i in range(1, n):
        attitude, peer, idx = scores[i]
        
        if max_peer > peer:  # 탈락
            if idx == 1:  # 주의: 완호가 탈락한 경우
                return -1
            continue
            
        max_peer = max(peer, max_peer)  # 갱신 시점 주의: 탈락하는 참가자는 이전에 걸러내기
        candidates.append((attitude + peer, idx))
    
    candidates.sort(key=lambda x: (-x[0]))  # 후보들
    
    cnt = 1
    rank = 1
    if candidates[0][1] == 1:   # 주의: 완호가 첫번째인 경우
        return 1
    
    for i in range(1, len(candidates)):
        if candidates[i-1][0] == candidates[i][0]:  # 같으면 카운팅 올리기
            cnt += 1
            continue

        rank += cnt
        cnt = 1
        
        if candidates[i][1] == 1:
            return rank

    return rank