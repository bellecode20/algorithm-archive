def go(oil,total,city):
    global mn_cost

    if city==N-1:
        mn_cost=min(mn_cost,total)
        return
    if oil>sum(costs):
        return
    if total>=mn_cost:
        return
    if (oil,city) in visited and visited[(oil,city)]<=total:
        return
    visited[(oil,city)]=total
    if distance[city]<=oil:
        go(oil-distance[city],total,city+1)
    
    
    go(oil+1,total+costs[city],city)

N=int(input())
distance=list(map(int,input().split()))
costs=list(map(int,input().split()))
mn_cost=float("inf")
visited={}

go(0,0,0)    #현재기름보유량, 총 비용, 현재 위치한 도시

print(mn_cost)