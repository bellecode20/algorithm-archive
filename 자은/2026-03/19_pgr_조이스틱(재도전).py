'''
어느 위치에서 방향을 딱 한번 틀 것인가를 찾아야함
안트는게 유리하면 말고

[현재 위치에서 가려는 곳으로 이동하는데 필요한 조작횟수]
오른쪽으로 갈때 필요한 조작횟수: 가려는 인덱스-현재 인덱스
왼쪽으로 갈때 필요한 조작횟수: 단어길이-(가려는 인덱스-현재 인덱스)
--> 오른쪽과 왼쪽 중 값이 더 작은 것을 선택
'''

def solution(name):
    answer = 0
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Done=[False]*len(name)

    for i in range(len(name)):
        if name[i]=='A':
            Done[i]=True
            continue
        a_idx=alphabet.index(name[i]) #찾아야하는 알파벳의 위치인덱스
        if a_idx<= 26-a_idx:    #위로 이동하는게 유리한 경우
            answer+=a_idx
        else:
            answer+=26-a_idx #아래로 이동하는게 유리한 경우
            
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        move = min(move, i + (n - next_i) + min(i, n - next_i))
    answer+=move    
    return answer