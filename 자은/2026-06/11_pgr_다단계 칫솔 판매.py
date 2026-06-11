def solution(enroll, referral, seller, amount):
    ans = [0]*len(enroll)
    en={}
    for i in range(len(enroll)):    #각 판매원들 인덱스저장
        en[enroll[i]]=i
        
    def dist(s,a):
        nonlocal ans
        
        if a>=10:
            ref=a//10   #추천인몫
            mine=a-ref    #내몫
            if referral[en[s]]!="-":
                dist(referral[en[s]],ref)
                
        else:mine=a
            
        ans[en[s]]+=mine    #내몫 판매량 집계
        
    for i in range(len(seller)):
        se=seller[i]
        am=amount[i]*100
        dist(se,am)
    
    return ans