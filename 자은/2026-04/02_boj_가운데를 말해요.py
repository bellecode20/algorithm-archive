import heapq
from sys import stdin

N=int(stdin.readline())
left=[]
right=[]
for _ in range(N):
    if len(left) <= len(right):
        heapq.heappush(left,-int(stdin.readline()))
    else:
        heapq.heappush(right,int(stdin.readline()))
    
    if left and right and -left[0]>right[0]:
        mx=heapq.heappop(left)
        mn=heapq.heappop(right)

        heapq.heappush(left,-mn)
        heapq.heappush(right,-mx)
    print(-left[0])
    
    