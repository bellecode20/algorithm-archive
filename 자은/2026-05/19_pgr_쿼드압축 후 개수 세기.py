def solution(arr):

    def compress(x,y,n):
    
        check=arr[x][y] #첫번째 값이랑 같은지 체크
        is_same=True

        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != check:
                    is_same=False
                    break
            if is_same==False:
                break
        
        if is_same:
            answer[check]+=1
        else:
            compress(x,y,n//2)
            compress(x,y+n//2,n//2)
            compress(x+n//2,y,n//2)
            compress(x+n//2,y+n//2,n//2)
                
                
    answer = [0,0]  #0의 개수,1의 개수
    compress(0,0,len(arr))
    
    return answer