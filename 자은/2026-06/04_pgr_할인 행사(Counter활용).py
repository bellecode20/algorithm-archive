'''
딕셔너리로 해보려다가 이후에 어떻게 해야할지 아이디어가 안떠올랏는데
Counter쓰니까 좋네
'''

from collections import Counter

def solution(want, number, dis):
    ans = 1
    
    buy={}
    for i in range(len(want)):
        buy[want[i]]=number[i]
    
    for i in range(len(dis)-9):
        if buy==Counter(dis[i:i+10]):
            ans+=1

    return ans