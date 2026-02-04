from collections import defaultdict
for _ in range(int(input())):
    W = input()
    K=int(input())
    min_len,mx_len=len(W),0
    char_dict=defaultdict(list)
    for i in range(len(W)): char_dict[W[i]].append(i)
    for lst in char_dict.values():
        if len(lst)>=K:
            for i in range(len(lst)-K+1):
                chars_len = lst[i+K-1]-lst[i]+1
                min_len=min(min_len,chars_len)
                mx_len=max(mx_len,chars_len)
    if mx_len==0:print(-1)
    else:print(min_len, mx_len)