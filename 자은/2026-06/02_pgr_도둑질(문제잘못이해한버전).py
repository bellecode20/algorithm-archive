'''
인접한 두 집이 털리면 경보가 울린다를
내 집을 기준으로 양쪽 집이 털리면 경보가 울린다로 잘못 이해함
'''

def solution(money):
    answer = 0
    memo=[0]*len(money) #각 집의 인접한 집이 털렸는지 체크(최대 2)
    n=len(money)
    
    def steal(i,total):
        nonlocal answer
        
        if i>=n:
            answer=max(answer,total)
            return
        
        #안훔칠때
        steal(i+1,total)
        
        #훔칠때
        total+=money[i]
        memo[(i+n+1)%n]+=1  #왼쪽
        memo[(i+1)%n]+=1    #오른쪽
        if memo[(i+n+1)%n]>=2 or memo[(i+1)%n]>=2:  #인접한 두집이 털린집이 있는지
            answer=max(answer,total)
        else:
            steal(i+1,total)
        
        #백업
        total-=money[i]
        memo[(i+n+1)%n]-=1  #왼쪽
        memo[(i+1)%n]-=1    #오른쪽
        
    steal(0,0)
    
    return answer