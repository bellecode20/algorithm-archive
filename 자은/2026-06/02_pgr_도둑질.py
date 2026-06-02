def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    # 0번 집을 털때
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집 제외
        dp1[i] = max(dp1[i - 1],money[i]+dp1[i - 2])#안털때,털때(지금집+전전집)중 더 큰거
    
    # 0번 집을 안털때
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1],money[i]+dp2[i - 2])

    return max(dp1[-2], dp2[-1])