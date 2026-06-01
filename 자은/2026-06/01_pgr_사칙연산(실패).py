def solution(arr):
    answer = float("-inf")
    
    def cal(a,b,op):
        if op=='+':return a+b
        if op=='-':return a-b
    
    def solve(c,ans):   #현재 연산자 인덱스
        nonlocal answer
        
        if c>=len(arr):
            answer=max(answer,ans)
            return
        
        #순서대로 계산버전
        solve(c+2,cal(ans,int(arr[c+1]),arr[c]))
        
        #뒤에꺼를 먼저계산버전
        if c<len(arr)-3:
            nxt=cal(int(arr[c+1]),int(arr[c+3]),arr[c+2])
            solve(c+4,cal(ans,nxt,arr[c]))
    
    solve(1,int(arr[0]))
    return answer