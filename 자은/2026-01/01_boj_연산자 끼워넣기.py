def solve(n,cnt, plus,minus,sub,div):
    global min_result, max_result

    if n==N-1:
        max_result=max(max_result,cnt)
        min_result=min(min_result,cnt)
        return

    if plus>0:
        solve(n+1,cnt+A[n+1], plus-1,minus,sub,div)
    if minus>0:
        solve(n+1,cnt-A[n+1], plus,minus-1,sub,div)
    if sub>0:
        solve(n+1,cnt*A[n+1], plus,minus,sub-1,div)
    if div>0:
        solve(n+1,int(cnt/A[n+1]), plus,minus,sub,div-1)

N=int(input())
A=list(map(int,input().split()))
plus,minus,sub,div=map(int,input().split())

max_result=float("-inf")
min_result=float("inf")

solve(0,A[0],plus,minus,sub,div)
print(max_result)
print(min_result)



