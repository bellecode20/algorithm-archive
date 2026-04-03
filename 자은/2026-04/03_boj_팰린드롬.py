N=int(input())
nums=list(map(int,input().split()))
M=int(input())
memo_t=set()
memo_f=set()
for _ in range(M):
    S,E=map(int,input().split())
    S-=1
    E-=1

    cnt=(E-S+1)//2

    find=True
    temp=[]
    for i in range(cnt):
        if (S+i,E-i) in memo_t:
            break
        if (S+i,E-i) in memo_f:
            find=False
            break
        if nums[S+i] != nums[E-i]:
            memo_f.add((S+i,E-i))
            find=False
            break
        temp.append((S+i,E-i))
    
    if find:
        print(1)
        memo_t.update(temp)
    else:
        memo_f.add((S,E))
        print(0)

