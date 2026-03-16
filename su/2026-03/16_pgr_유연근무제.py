def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    
    def get_sec(timestamp):  # 시간초로 변환
        result = 0
        hour = (timestamp // 100)
        minutes = (timestamp % 100)
        result += (hour * 60 * 60) + minutes * 60
        return result
    
    for i in range(n):
        goal_t = get_sec(schedules[i])
        goal_t += 600  # 10분 추가
        
        today = startday
        is_success = True
        
        for j in range(7):
            if today == 6 or today == 7:
                today += 1
                if today == 8:
                    today = 1
                continue
                    
            work_t = get_sec(timelogs[i][j])
            
            if work_t > goal_t:
                is_success = False
                break
                
                         
            today += 1
            if today == 8:
                today = 1
                
        if is_success:
            answer += 1
            
    
    return answer