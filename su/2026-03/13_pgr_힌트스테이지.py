def solution(cost, hint_info):
    min_total_cost = int(1e9)
    n = len(cost)
    
    def dfs(stg_idx, cur_cost, hints):
        nonlocal min_total_cost
        
        # 1. 현재 스테이지에서 쓸 수 있는 힌트 개수 계산
        my_hints = hints.count(stg_idx + 1)
        
        # 2. 스테이지 클리어 비용 적용 (보유 힌트가 너무 많으면 최대 할인 적용)
        max_discount_idx = len(cost[stg_idx]) - 1
        use_hints = min(my_hints, max_discount_idx)
        cur_cost += cost[stg_idx][use_hints]
        
        # 만약 이미 최솟값보다 비싸졌다면 더 계산할 필요 없음
        if cur_cost >= min_total_cost:
            return

        # 3. 마지막 스테이지라면 결과 기록 후 종료
        if stg_idx == n - 1:
            min_total_cost = min(min_total_cost, cur_cost)
            return
        
        # 구매X 
        dfs(stg_idx + 1, cur_cost, hints)
        
        # 구매O
        if stg_idx < len(hint_info):
            bundle_price = hint_info[stg_idx][0]
            new_hints = hint_info[stg_idx][1:] # 번들에 들어있는 힌트들
            
            # 비용에 번들 가격 추가, 주머니에 새 힌트들 합치기
            dfs(stg_idx + 1, cur_cost + bundle_price, hints + new_hints)
        
    # 0번 스테이지부터, 비용 0원, 빈 주머니로 시작
    dfs(0, 0, [])
    
    return min_total_cost