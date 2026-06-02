from functools import lru_cache #호출 결과가 이미 캐시되어 있으면 함수를 실행하지 않고 캐시 결과를 반환해줌
import sys
sys.setrecursionlimit(10**8) # 재귀 제한을 1,000에서 1억(10^8)으로 늘려주기(안하면 1000이 넘을시 강제종료됨)

def solution(money):
    ans=0
    
    @lru_cache(maxsize=None)
    def steal(i,flag):  #인덱스, 첫번째집 털이 여부
        ()
        if flag:end=len(money)  #첫번째집을 안털때: 종착지(end)=마지막집까지
        else:end=len(money)-1   #첫번째집을 털때: 종착지(end)=마지막집 전까지
        
        if i==end-1 or i==end-2:    #종착지-1,종착지-2는 뒤뒤집,뒤뒤뒤집을 확인 못하니까 그냥 현재집만 털기
            return money[i]
        if i >= end:    #종착지를 넘어서면
            return 0
        
        
        #현재집+ (뒤뒤집 털때or 뒤뒤뒤집 털때)
        return money[i] + max(steal(i+2,flag), steal(i+3,flag))
    
    #0번집 털때, 1번집 털때, 2번집 털때(0번집 안텀) 중 제일 큰거
    ans=max(steal(0,0), steal(1,1), steal(2,1))
    
    return ans