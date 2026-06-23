def solution(gems):
    a,b=0,len(gems)-1
    total=len(set(gems))    #총 보석종류 개수
    l,r=0,0
    cart={gems[0]:1}
    
    while l<len(gems) and r<len(gems):
        
        if len(cart)==total:    #보석 종류를 다 담았을때
            if r-l< b-a:    #최소면 갱신
                a,b=l,r
            else:   #아니라면 l구간 옮겨서 크기 줄이기
                cart[gems[l]]-=1
                if cart[gems[l]]==0:
                    del cart[gems[l]]
                l+=1
        
        else:
            r+=1
            if r>=len(gems):break
    
            cart[gems[r]]=cart.get(gems[r],0)+1
    
        
    return [a+1,b+1]