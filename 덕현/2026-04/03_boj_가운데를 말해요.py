'''
BOJ 1655 가운데를 말해요

입력:
N
left []
right []

구조:
우선순위 큐 써서 왼오 구분하고 작은거 큰거넣기
최대값 비교해서 교환

출력 한번에해야 시간초과 안난다함
'''
import heapq

N = int(input())

left = []
right = []
ans = []

for _ in range(N):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(right) > 0 and -left[0] > right[0]:
        a = -heapq.heappop(left)
        b = heapq.heappop(right)

        heapq.heappush(left, -b)
        heapq.heappush(right, a)

    ans.append(str(-left[0]))

print('\n'.join(ans))