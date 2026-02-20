def comb(n,c,s):

    if n==6:
        print(*c)
        return
    
    for i in range(s,k):
        comb(n+1,c+[lst[i]],i+1)

while True:
    lst=list(map(int,input().split()))
    if lst[0]==0:break
    k=lst[0]
    lst=lst[1:]

    comb(0,[],0)
    print()