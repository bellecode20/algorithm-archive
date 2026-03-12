'''
프로그래머스 468377 힌트 스테이지

입력:
cost
hint

구조:
dfs + dp ?
현재 스테이지부터 마지막 스테이지까지 힌트 개수 들고 감
현재 스테이지에서 번들을 안 사는 경우 or 사는 경우
둘 중 최소 비용
'''
def solution(cost, hint):

    n = len(cost)
    INF = float('inf')
    dp = {}

    def make_key(idx, arr):
        s = str(idx) + '/'
        for i in range(len(arr)):
            s += str(arr[i]) + ','
        return s

    def dfs(idx, arr):

        if idx == n:
            return 0

        key = make_key(idx, arr)
        if key in dp:
            return dp[key]

        use = arr[0]
        if use > n-1:
            use = n-1

        ans = INF

        next_arr = []
        for i in range(1, len(arr)):
            cur = arr[i]
            if cur > n-1:
                cur = n-1
            next_arr.append(cur)

        cur_cost = cost[idx][use] + dfs(idx+1, next_arr)
        if ans > cur_cost:
            ans = cur_cost

        if idx < n-1:

            buy_arr = []
            for i in range(1, len(arr)):
                cur = arr[i]
                if cur > n-1:
                    cur = n-1
                buy_arr.append(cur)

            price = hint[idx][0]

            for k in range(1, len(hint[idx])):
                num = hint[idx][k] - 1
                pos = num - (idx+1)
                buy_arr[pos] += 1

            buy_cost = cost[idx][use] + price + dfs(idx+1, buy_arr)

            if ans > buy_cost:
                ans = buy_cost

        dp[key] = ans
        return ans

    start = [0]*n
    return dfs(0, start)