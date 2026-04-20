def cal(a,op,b):
    if op=='+':return a+b
    if op=='-':return a-b
    if op=='*':return a*b

def dfs(total,idx): #지금까지의 값, 현재 인덱스
    global answer

    if idx>=N:
        answer=max(answer,total)
        return
    
    #다음 숫자에 괄호 추가 안하는 경우
    nxt=cal(total,ex[idx],int(ex[idx+1]))   #현재까지의 값,현재 연산자, 다음 숫자
    dfs(nxt,idx+2)

    #다음 숫자에 괄호 추가하는 경우
    if idx+2<N:
        braket=cal(int(ex[idx+1]),ex[idx+2],int(ex[idx+3])) #다음괄호 미리 계산
        nxt_b=cal(total,ex[idx],braket) #현재까지의 값, 현재 연산자, 괄호로 계산된 다음 값
        dfs(nxt_b,idx+4)

N=int(input())
ex=list(input())
answer=-float("inf")

dfs(int(ex[0]),1)   #첫번째 연산자부터 시작
print(answer)