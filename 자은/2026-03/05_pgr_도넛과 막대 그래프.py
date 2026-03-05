from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]  #생성, 도넛, 막대, 8자
    info=defaultdict(lambda:[0,0])
    
    for a,b in edges:
        info[a][1]+=1
        info[b][0]+=1
    
    for k,v in info.items():
        in_v=v[0]
        out_v=v[1]
        
        if in_v==0 and out_v>=2:
            answer[0]=k
        elif in_v>=1 and out_v==0:
            answer[2]+=1
        elif in_v>=2 and out_v==2:
            answer[3]+=1
            
    answer[1]=info[answer[0]][1]-answer[2]-answer[3]
        
    return answer