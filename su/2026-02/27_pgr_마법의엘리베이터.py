def solution(storey):
    answer = 0
    
    while storey > 0:
        remainder = storey % 10
        next_digit = (storey // 10) % 10
        
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10  # 올림 처리
        elif remainder < 5:
            answer += remainder
        else: # remainder == 5 인 경우
            if next_digit >= 5:
                answer += 5
                storey += 10 # 다음 자릿수가 크면 올림
            else:
                answer += 5
                
        storey //= 10 # 다음 자릿수로 이동
        
    return answer