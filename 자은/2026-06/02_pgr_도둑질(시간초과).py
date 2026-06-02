def solution(money):
    ans = 0
    is_valid=[True]*len(money)
    n=len(money)
    
    def steal(i,total):
        nonlocal ans
        
        if i>=n:
            ans=max(ans,total)
            return
        
        #안훔칠때
        steal(i+1,total)
        
        #훔칠때
        if is_valid[i]:
            is_valid[(i+n+1)%n]=False   #왼쪽집은 이제 못텀
            is_valid[(i+1)%n]=False     #오른쪽집은 이제 못텀
            total+=money[i]
            steal(i+1,total)
            #백업
            total-=money[i]
            is_valid[(i+n+1)%n]=True
            is_valid[(i+1)%n]=True
    
    steal(0,0)
    
    return ans