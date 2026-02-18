'''
나를 제외한 계란들중에서 하나를 뽑아야함
깨진계란은 다음 뽑기에서 제외시켜야함
'''
def pick(n,b_cnt):
    global result

    if result >= min(N, b_cnt + (N - n) * 2):
        return

    if n==N:
        result=max(result,b_cnt)
        return
    
    if e[n][0]<=0:
        pick(n+1,b_cnt)
        return

    S,W=e[n][0],e[n][1]
    stop=True

    for j in range(N):
        if j==n:continue
        if e[j][0]<=0:continue
        stop=False
        S2,W2=e[j][0],e[j][1]
        e[n][0]-=W2
        e[j][0]-=W
        pick(n+1,b_cnt+int(e[n][0]<=0)+int(e[j][0]<=0))
        e[n][0]=S
        e[j][0]=S2

    if stop:
        result=max(result,N-1)
        return

N=int(input())
e=[list(map(int,input().split())) for _ in range(N)]
result=0

pick(0,0)
print(result)
