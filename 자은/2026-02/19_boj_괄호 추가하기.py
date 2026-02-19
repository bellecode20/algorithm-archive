def cal(a,op,b):
    if op=='+':return a+b
    if op=='-':return a-b
    if op=='*':return a*b

def dfs(idx, c):
    global result

    if idx>=N:
        result=max(result,c)
        return

    next=cal(c,ex[idx],int(ex[idx+1]))
    dfs(idx+2,next)

    if idx+2<N:
        bracket= cal(int(ex[idx+1]),ex[idx+2],int(ex[idx+3]))
        next_b=cal(c,ex[idx],bracket)
        dfs(idx+4,next_b)

N=int(input())
ex=input()
result=-float("inf")

dfs(1,int(ex[0]))
print(result)
