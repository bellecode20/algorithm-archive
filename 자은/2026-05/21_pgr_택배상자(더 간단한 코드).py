'''
이렇게 간단하다는걸 다른사람 코드 보고나서 깨달았다ㅠㅠ
그냥 일단 stack에 집어넣고 마지막값만 확인하면 되는데
나는 현재 순서가 아닐때만 넣는 임시공간용으로 stack을 만들어서 코드가 복잡해짐
'''

def solution(order):
    answer = 0
    temp=[] #임시로 두는곳
    cur=1   #현재 컨베이어벨트에서 나온 택배번호
    idx=0   #현재 트럭에 실어야하는 상자순서인덱스번호
    
    while cur<=len(order):
        temp.append(cur)
        
        while temp[-1]==order[idx]:
            temp.pop()
            idx+=1
            if not temp:break
            
        cur+=1
    
    return idx