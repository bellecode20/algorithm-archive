def solution(n, left, right):
    ans = []
    num=1
    if left>n:
        num=left//n+1
        right-=n*(left//n)
        left%=n
        
    while num<=n:
        if len(ans)>=right:break
        
        for i in range(num):
            ans.append(num)
        for i in range(num+1,n+1):
            ans.append(i)
        
        num+=1
        
    return ans[left:right+1]