def solution(cards):
    for i in range(len(cards)):cards[i]-=1  #인덱스 편의성을 위해 1씩 빼주기
    opened=[False]*len(cards)
    cnt=0   #연 상자 개수
    turn=0
    boxes=set()
    
    def open_box(n):
        nonlocal temp,cnt
        
        nxt=cards[n]
        if opened[nxt]:return  #이미 열려있는 상자면 종료
        opened[nxt]=True    #상자열기
        cnt+=1              #연 상자 개수 카운트+1
        temp.append(nxt)
        open_box(nxt)
    
    while cnt<len(cards):   #모든 상자를 열때까지
        temp=[turn]
        opened[turn]=True   #시작상자 열기
        cnt+=1  #연 상자 개수 카운트+1
        open_box(turn)
        boxes.add(tuple(temp))
        while turn<len(cards) and opened[turn]:    #열지않은 상자가 나올때까지
            turn+=1

    if len(boxes)<=1:return 0
    boxes=list(boxes)
    boxes.sort(key=lambda x:len(x))   
    return len(boxes[-1])*len(boxes[-2])