def solution(A, B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort()
    bi = -1
    
    for i in range(n):
        while True:  # B팀이 이기는 수 인덱스 찾기
            bi += 1
            if bi == n:
                return answer
            
            if A[i] < B[bi]:
                answer += 1
                break
                
    return answer