def solution(n, st, w):
    ans = 0
    un=[]
    
    if st[0]-w>0:un.append(st[0]-w-1)
    for i in range(1,len(st)):
        un.append((st[i]-w)-(st[i-1]+w)-1)
    if st[-1]+w<n:un.append(n-(st[-1]+w))
    
    l=w*2+1
    for apts in un:
        if apts%l:ans+=apts//l+1
        else:ans+=apts//l
    return ans