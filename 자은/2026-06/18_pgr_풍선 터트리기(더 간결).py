def solution(a):
    n=len(a)
    if n==1:return 1
    if n==2:return 2
    
    pos={a[0],a[-1]}
    
    #각 자리에서 왼쪽 최솟값보다 내가 더 작은지
    mn=a[0]
    for i in range(1,n-1):
        if mn>a[i]:
            mn=a[i]
            pos.add(a[i])
    
    #각 자리에서 오른쪽 최솟값보다 내가 더 작은지
    mn=a[-1]
    for i in range(n-2,0,-1):
        if mn>a[i]:
            mn=a[i]
            pos.add(a[i])

    return len(pos)