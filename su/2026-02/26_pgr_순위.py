def solution(n, results):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        matrix[win][lose] = 1   # 승리
        matrix[lose][win] = -1  # 패배

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
                    matrix[j][i] = -1
                elif matrix[i][k] == -1 and matrix[k][j] == -1:
                    matrix[i][j] = -1
                    matrix[j][i] = 1

    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if matrix[i][j] != 0:
                count += 1
        
        if count == n - 1:
            answer += 1
            
    return answer