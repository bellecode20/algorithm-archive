def solution(order):
    answer = 0
    temp=[] #임시로 두는곳
    cur=1   #현재 컨베이어벨트에서 나온 택배번호
    idx=0   #현재 트럭에 실어야하는 상자순서인덱스번호
    
    while cur<=len(order) and idx<len(order):
        
        if cur==order[idx]:
            answer+=1
            if idx<len(order)-1:idx+=1
            if cur<len(order):cur+=1
        else:
            if cur<order[idx]:
                while cur!=order[idx]:
                    temp.append(cur)
                    cur+=1              
                answer+=1
                idx+=1
                if cur<len(order):
                    cur+=1
            else: 
                if temp and temp[-1]==order[idx]:
                    temp.pop() 
                    answer+=1
                    idx+=1
                else:
                    break
                
    
    return answer