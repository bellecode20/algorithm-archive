'''
프로그래머스 258711 도넛과 막대 그래프

구조:
각 정점의 in/out 개수 세기
생성 정점: in = 0 이고 2 <= out
막대: out = 0 인 정점 개수
8자: 2 <= in 이고 out >=2  인 정점 개수
도넛: 생성정점 out 개수-(막대+8자)

틀린 이유 : 정점노드 순서대로 들어오는 보장이 없음
'''

def solution(edges):
    nodes = set()
    in_cnt = {}
    out_cnt = {}

    for a, b in edges:
        nodes.add(a)
        nodes.add(b)

        out_cnt[a] = out_cnt.get(a, 0) + 1
        in_cnt[b] = in_cnt.get(b, 0) + 1

        if a not in in_cnt:
            in_cnt[a] = in_cnt.get(a, 0)
        if b not in out_cnt:
            out_cnt[b] = out_cnt.get(b, 0)

    created = 0
    for v in nodes:
        if in_cnt.get(v, 0) == 0 and out_cnt.get(v, 0) >= 2:
            created = v
            break

    bar = 0
    eight = 0

    for v in nodes:
        if out_cnt.get(v, 0) == 0:
            bar += 1
        elif in_cnt.get(v, 0) >= 2 and out_cnt.get(v, 0) >= 2:
            eight += 1

    donut = out_cnt.get(created, 0) - bar - eight

    return [created, donut, bar, eight]