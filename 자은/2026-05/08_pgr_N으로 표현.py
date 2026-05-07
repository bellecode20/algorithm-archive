def solution(N, number):
    answer = 0
    dp=[set() for _ in range(9)]    #N을 1~9번 사용할때 나오는 값들 전부 저장
    '''
    예를 들어 N=5일때,
    5를 1번 사용할 때 => {5}
    5를 2번 사용할 때 => 1번과 1번을 활용하여 사칙연산 =>  {55, (5+5), (5*5), (5/5), (5-5)}
    5를 3번 사용할 때 => 1번과 2번을 활용하여 사칙연산 => {555, 5+(5+5), 5*(5+5), 5/(5+5), 5-(5+5), 5+(5*5), 5*(5*5), 5/(5*5), .....}
    5를 4번 사용할 때 => 1번과 3번, 또는 2번과 2번을 활용하여 사칙연산
    N을 5번 사용하는 경우 => 1번과 4번, 2번과 3번을 활용하여 사칙연산
    '''
    
    for i in range(1,9):    #N을 1~9번 사용할때
        dp[i].add(int(str(N)*i))    #N,NN,NNN ...
        for j in range(i//2+1):
            for start in dp[j]:
                for end in dp[i-j]:
                    dp[i].add(start+end)
                    dp[i].add(start-end)
                    dp[i].add(end-start)
                    dp[i].add(start*end)
                    if end != 0:
                        dp[i].add(start//end)
                    if start !=0:
                        dp[i].add(end//start)
        if number in dp[i]:
            return i
    return -1