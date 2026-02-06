def find(n):
    global cnt, rain
    for j in range(n+1,W):
        if blocks[j]>=blocks[n]:
            if len(skipped)==0:return
            water=blocks[n]*len(skipped)
            for k in skipped:water-=k
            rain+=water
            return
        else:
            cnt+=1
            skipped.append(blocks[j])       

H, W=map(int,input().split())
blocks=list(map(int,input().split()))
rain=cnt=0
for i in range(W-2):
    if cnt:
        cnt-=1
        continue
    skipped=[]
    find(i)
    if len(skipped)==(W-i-1):
        blocks[i]=max(skipped)
        skipped=[]
        cnt=0
        find(i)
print(rain)