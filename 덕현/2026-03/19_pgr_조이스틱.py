'''
프로그래머스 42860 조이스틱

입력:
name

구조:
각 문자 위아래 조작 횟수 더하기
좌우 이동 최소값 따로 구하기
중간에 연속된 A 구간 기준으로
오른쪽 갔다가 돌아오기
왼쪽부터 처리
while 돌면서 처리하면될듯
'''


def solution(name):
    ans = 0
    n = len(name)

    for i in range(n):
        cur = ord(name[i]) - ord('A')
        ans += min(cur, 26 - cur)

    move = n - 1

    for i in range(n):
        nxt = i + 1

        while nxt < n and name[nxt] == 'A':
            nxt += 1

        cur_move = i * 2 + (n - nxt)

        if move > cur_move:
            move = cur_move

        cur_move = i + (n - nxt) * 2
        if move > cur_move:
            move = cur_move

    ans += move

    return ans