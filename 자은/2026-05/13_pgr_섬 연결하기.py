def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    linked=set()
    linked.add(costs[0][0])
    
    while len(linked) != n:
        for v in costs:
            if v[0] in linked and v[1] in linked:
                continue
            if v[0] in linked or v[1] in linked:
                linked.update([v[0],v[1]])
                answer+=v[2]
                break
    return answer