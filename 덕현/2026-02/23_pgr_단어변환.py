'''
프로그래머스 43163 단어 변환

입력:
begin, target, words

구조:
- target이 words에 없으면 바로 0
- bfs
- 한 글자만 다른 단어로만 이동
- 처음 target 도착한 depth가 답
'''

def one_diff(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    visited = [False] * n


    q = [(begin, 0)]
    head = 0

    while head < len(q):
        cur, d = q[head]
        head += 1

        if cur == target:
            return d

        for i in range(n):
            if not visited[i] and one_diff(cur, words[i]):
                visited[i] = True
                q.append((words[i], d + 1))

    return 0