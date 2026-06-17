def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        # 홀수 길이의 팰린드롬
        left = i
        right = i
        temp_len = 0
        while left >= 0 and right < n:
            if s[left] == s[right]:
                temp_len = right - left + 1
                right += 1
                left -= 1
                continue
            break
        
        # 짝수 길이의 팰린드롬
        left = i
        right = i+1
        temp_len_2 = 0
        while left >= 0 and right < n:
            if s[left] == s[right]:
                temp_len_2 = right - left + 1
                right += 1
                left -= 1
                continue
            break
            
        
        # print(temp_len, temp_len_2, i)
        answer = max(temp_len, temp_len_2, answer) 
        
    return answer