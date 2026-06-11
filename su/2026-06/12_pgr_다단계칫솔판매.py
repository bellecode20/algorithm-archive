# 
from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    idx_info = defaultdict(int)
    parents_info = defaultdict(str)
    result = [0] * len(enroll)
    
    for i in range(len(enroll)):
        parents_info[enroll[i]] = referral[i]
        idx_info[enroll[i]] = i
    
    def dfs(name, m):
        if name == "-":
            return
        
        if math.floor(m * 0.1) == 0:  # 나눌 필요 없는 경우
            result[idx_info[name]] += m
            return
        else:
            result[idx_info[name]] += m - int(m * 0.1)
        
        p = parents_info[name]
        next_m = int(m * 0.1)
        dfs(p, next_m)
        
    
    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)
    
    return result
