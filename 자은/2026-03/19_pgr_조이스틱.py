'''
채점 결과
정확성: 74.1
합계: 74.1 / 100.0


[현재 위치에서 가려는 곳으로 이동하는데 필요한 조작횟수]
오른쪽으로 갈때 필요한 조작횟수: 가려는 인덱스-현재 인덱스
왼쪽으로 갈때 필요한 조작횟수: 단어길이-(가려는 인덱스-현재 인덱스)
--> 오른쪽과 왼쪽 중 값이 더 작은 것을 선택
'''

def solution(name):
    answer = 0
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Done=[False]*len(name)

    trans_a=[0]*len(name)   #각 위치마다 알파벳 변환하는데 필요한 조작횟수
    for i in range(len(name)):
        a_idx=alphabet.index(name[i]) #찾아야하는 알파벳의 위치인덱스
        if a_idx<= 26-a_idx:    #위로 이동하는게 유리한 경우
            trans_a[i]=a_idx
        else:
            trans_a[i]=26-a_idx #아래로 이동하는게 유리한 경우
    for i in range(len(Done)):
        if trans_a[i]==0:   #A일경우
            Done[i]=True
            
    cur=0   #현재 위치 

    while True:
        
        if not Done[cur]:
            answer+=trans_a[cur]
            Done[cur]=True
            
        if all(Done):
            break
            
        for_go=[0]*len(name)
        for i in range(len(name)):
            right=abs(i-cur)
            left=len(name)-right
            
            if right<=left:
                for_go[i]=right
            else:
                for_go[i]=left
        mn_go=len(name)
        mn_idx=0
        for i in range(len(for_go)):    #가장 적은횟수로 이동하는 곳 찾기
            if Done[i] or i==cur:
                continue
            if mn_go>for_go[i]:
                mn_go=for_go[i]
                mn_idx=i
                
        answer+=mn_go
        cur=mn_idx
        
    return answer