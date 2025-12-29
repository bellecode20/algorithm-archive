def cal(ateam,bteam):
    ateam_sum=0
    bteam_sum=0

    for i in range(N//2):
        for j in range(N//2):
            ateam_sum+=arr[ateam[i]][ateam[j]]
            bteam_sum+=arr[bteam[i]][bteam[j]]
    return abs(ateam_sum-bteam_sum)

def solve(n,ateam,bteam):
    global min_ans
    if n ==N:
        if len(ateam)==len(bteam):
            min_ans=min(min_ans,cal(ateam,bteam))
        return

    solve(n+1,ateam+[n],bteam)
    solve(n+1,ateam,bteam+[n])

    

N= int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
min_ans=float("inf")

solve(0,[],[])

print(min_ans)