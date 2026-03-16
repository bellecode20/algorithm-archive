def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        hour=schedules[i]//100
        minute=schedules[i]%100
        minute+=10
        if minute>=60:
            hour+=1
            minute%=60
        
        day=startday
        success=True
        for j in range(7):
            if day<6:   #평일일때만 검사
                work_h=timelogs[i][j]//100
                work_m=timelogs[i][j]%100
                
                if work_h>hour: 
                    success=False
                    break
                elif work_h==hour and work_m>minute:
                    success=False
                    break
            day=(day%7)+1
        if success:
            answer+=1
                
    return answer