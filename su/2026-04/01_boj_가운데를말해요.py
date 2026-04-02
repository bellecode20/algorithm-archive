import heapq
from sys import stdin

N=int(stdin.readline())

left = []
right = []

for _ in range(N):
    x = int(stdin.readline())
    
    if len(left) == len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    
    if left and right and -left[0] > right[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)
    
    print(-left[0])
