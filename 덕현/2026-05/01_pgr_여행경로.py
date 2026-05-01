'''
프로그래머스 여행경로

입력:
tickets

구조:
출발 기준 해서 도착
갈곳 없으면 ans
뒤집기
'''

def solution(tickets):
    graph = {}
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    for key in graph:
        graph[key].sort(reverse=True)

    stack = []
    stack.append('ICN')

    answer = []
    while stack:
        cur = stack[-1]

        if cur not in graph or len(graph[cur]) == 0:
            answer.append(stack.pop())
        else:
            nxt = graph[cur].pop()
            stack.append(nxt)
    answer.reverse()
    return answer