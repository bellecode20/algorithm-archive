def str_cnt(n):
    k=0
    chars=""
    for i in range(n,len(W)):
        chars=chars[:]+W[i]
        if W[i]==W[n]:
            k+=1
            if k==K:
                break
    return len(chars)

T = int(input())
for t in range(T):
    W = input()
    K=int(input())
    min_len=len(W)
    max_len=0
    sucess=False
    for i in range(len(W)):
        cnt=W[i:].count(W[i])
        if cnt>=K:
            sucess=True
            chars_len=str_cnt(i)
            min_len=min(min_len,chars_len)

            if W[i]==W[i+chars_len-1]:
                max_len=max(max_len,chars_len)
    if sucess:
        print(min_len, max_len)
    else:
        print(-1)
