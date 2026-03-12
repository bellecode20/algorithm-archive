import math

def solution(signals):
    n = len(signals)
    periods = [sum(s) for s in signals]
    
    lcm_val = periods[0]
    for i in range(1, n):
        lcm_val = (lcm_val * periods[i]) // math.gcd(lcm_val, periods[i])
        
    for t in range(1, lcm_val + 1):
        all_yellow = True
        
        for i in range(n):
            g, y, r = signals[i]
            l = periods[i]
            
            current_time = (t - 1) % l
            
            if not (g <= current_time < g + y):
                all_yellow = False
                break
        
        if all_yellow:
            return t
            
    return -1