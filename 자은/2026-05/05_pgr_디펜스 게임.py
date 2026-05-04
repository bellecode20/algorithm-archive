import heapq

def solution(n, k, enemy):
    answer = 0
    
    heap=[] #적의수가 제일 많은 순으로 무적권 씀
    
    for i in range(len(enemy)):
        if n>= enemy[i]:    #해치울 병사가 남아있으면
            n-=enemy[i]
            heapq.heappush(heap,-enemy[i])
        elif k>0:   # 병사는 없는데 무적권이 남아있다면
            if heap and -heap[0]>enemy[i]:
                n+=-(heapq.heappop(heap))  #병사가 가장 많이 소모된라운드의 병사부활 
                n-=enemy[i] #현재라운드 병사 소모
                heapq.heappush(heap,-enemy[i])
            k-=1    #무적권 1개 소진(병사가 가장 많이 소모되는 라운드)
        else:
            answer=i
            break
        answer=i+1
    
    return answer