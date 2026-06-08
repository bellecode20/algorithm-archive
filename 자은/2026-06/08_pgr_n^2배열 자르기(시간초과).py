def solution(n, left, right):
    answer = []
    arr=[[0]*n for _ in range(n)]
    arr[0][0]=1
    
    def fill(num):
        nonlocal arr
        arr[num][num]=num+1
        for i in range(num):
            arr[i][num]=num+1 #열채우기
            arr[num][i]=num+1 #행채우기
        
    for i in range(1,n):fill(i)
    
    answer=sum(arr,[])
    answer=answer[left:right+1]
    
    return answer