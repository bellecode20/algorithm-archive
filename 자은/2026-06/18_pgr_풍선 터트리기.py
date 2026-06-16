def solution(a):
    answer = 2
    n=len(a)
    if n==1:return 1
    if n==2:return 2

    #각 자리에서 왼쪽 최솟값
    lmn=[0]*n
    mn=a[0]
    for i in range(n):
        lmn[i]=min(mn,a[i])
        mn=min(mn,a[i])

    #각 자리에서 오른쪽 최솟값
    rmn=[0]*n
    mn=a[-1]
    for i in range(n-1,-1,-1):
        rmn[i]=min(mn,a[i])
        mn=min(mn,a[i])

    for i in range(1,len(a)-1):
        if lmn[i]>=a[i] or rmn[i]>=a[i]:
            answer+=1

    return answer
