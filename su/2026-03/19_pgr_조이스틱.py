def solution(name):
    n = len(name)

    # 1. 세로 이동 비용
    answer = 0
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

    # 2. 가로 이동 비용
    move = n - 1  # 일단 오른쪽으로만 끝까지 가는 경우

    for i in range(n):
        next_idx = i + 1

        # i 다음부터 연속된 A 구간 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 오른쪽 갔다가 돌아오기 vs 반대부터 처리하기
        move = min(move, 2 * i + n - next_idx, i + 2 * (n - next_idx))

    return answer + move