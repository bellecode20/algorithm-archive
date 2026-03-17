def solve(idx,total,cnt):
    global answer,memo

    if idx==n:
        answer=max(answer,total)
        return
    
    if (idx, cnt) in memo and memo[(idx,cnt)]>=total:
        return
    
    memo[(idx,cnt)]=total

    solve(idx+1,total,0)
    if cnt<2:
        solve(idx+1,total+wine[idx],cnt+1)
    



n=int(input())
wine=[ int(input()) for _ in range(n)]
answer=0
memo={}

solve(0,0,0)
print(answer)