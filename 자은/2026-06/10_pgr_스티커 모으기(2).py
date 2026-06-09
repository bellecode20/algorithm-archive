def solution(sticker):
    answer = 0
    
    if len(sticker)==1:return sticker[0]
    if len(sticker)==2:return max(sticker)
    
    #첫번째 값을 포함할때
    dp1=[0]*len(sticker)
    dp1[0]=sticker[0]
    dp1[1]=sticker[0]
    for i in range(2,len(sticker)-1):
        dp1[i]=max(dp1[i-1],dp1[i-2]+sticker[i])
    
    #첫번째 값을 포함하지 않을때
    dp2=[0]*len(sticker)
    dp2[1]=sticker[1]
    dp2[2]=max(sticker[1],sticker[2])
    for i in range(2,len(sticker)):
        dp2[i]=max(dp2[i-1],dp2[i-2]+sticker[i])
        
    return max(max(dp1),max(dp2))