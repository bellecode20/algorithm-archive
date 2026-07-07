import heapq

def solution(k, tan):
    ans = 0
    t=set(tan)
    cnt={}
    for i in t:
        cnt[i]=0
    for i in tan:
        cnt[i]+=1
    
    heap=[]
    for c in cnt.values():
        heapq.heappush(heap,-c)
    
    total=0
    for i in range(len(heap)):
        ans+=1
        total+=-(heapq.heappop(heap))
        if total>=k:break
    
    return ans