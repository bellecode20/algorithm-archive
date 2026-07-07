from collections import defaultdict
import heapq

def solution(s):
    answer = []
    s=s[2:-2]
    s=(s.split('},{'))
    s=[list(map(int,t.split(',')))for t in s]
    d=defaultdict(int)
    
    for t in s:
        for n in t:
            d[n]+=1

    heap=[]
    for key,value in d.items():
        heapq.heappush(heap,(-value,key))
    
    for i in range(len(heap)):
        value,key=heapq.heappop(heap)
        answer.append(key)
    return answer