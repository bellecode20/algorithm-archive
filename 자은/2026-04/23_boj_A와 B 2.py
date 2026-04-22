def solve(t):
    global ans

    if t==S:
        ans=1
        return
    if len(t)==len(S):return
    
    if t[-1]=='A':solve(t[:-1])
    if t[0]=='B':solve(t[:0:-1])

S=input()
T=input()
ans=0

solve(T)
print(ans)