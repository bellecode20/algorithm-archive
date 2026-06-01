def solution(arr):
    #-를 기준으로 나누기 ex) [1,3+5,8]
    arr=''.join(arr).split('-')
    fst=sum([*map(int,arr[0].split('+'))])   #맨 앞의 값 계산
    
    mn=mx=0 #계산된 뒤의 값 최소,최대
    
    for ex in arr[:0:-1]:    #arr 뒤에서부터
        temp=[*map(int,ex.split('+'))]  #+를 기준으로 나누기 ex) [3+5] -> [3,5]
        
        #temp 최소값:모든 값을 음수로
        mn_t=-sum(temp)
        
        #temp 최대값:첫번째값만 음수로
        mx_t=-2*temp[0]-mn_t  #temp합계-temp첫번째값*2 (*2를 하는 이유: 위에서 더해진 첫번째값 빼기 위해서)
     
    
        #------------------------------------------------------------------------------------------------
        #괄호를 앞까지만치기,뒤쪽까지 치기(뒤쪽까지 칠 경우 뒤의 값 부호 변경)의 조합 중 최소값,최대값
        #-temp다 더한값==mn_t
        
        #최소값갱신
        #(temp최소값+뒤쪽 최소값, -(temp다 더한값+뒤쪽 최대값))
        
        #최대값갱신
        #(temp최대값+뒤쪽 최대값, -(temp다 더한값+뒤쪽 최소값))
        
        mn,mx=min(mn_t+mn,mn_t-mx),max(mx_t+mx,mn_t-mn) 
        
    return fst+mx