def solution(x, y, n):
    answer = 0
    if x==y:return 0
    before={x+n,x*2,x*3}
    if y in before:return 1

    cnt=1
    while True:
        mn=y+1
        cnt+=1
        new=set()
        for b in before:
            new.update([b+n,b*2,b*3])
            mn=min(mn,b+n,b*2,b*3)
        
        if y in new:
            answer=cnt
            break
        if mn>y:
            answer=-1
            break
        
        before=new
        
    return answer