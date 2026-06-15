def solution(s):
    n=len(s)
    for l in range(n,0,-1):
        for i in range(n-l+1):
            if s[i:i+l]==s[i:i+l][::-1]:
                return l
    return 1