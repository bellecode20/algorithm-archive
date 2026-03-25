'''
BOJ 13305 주유소

입력:
N
road
price

구조:
그리디??
왼쪽부터 보면서 지금까지 나온 가격 중 최소값 유지
현재 도로 길이는 그 최소 가격으로 구매
전체 비용 누적해서 답
'''
N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
cur = price[0]

for i in range(N - 1):

    if cur > price[i]:
        cur = price[i]

    ans += cur * road[i]

print(ans)