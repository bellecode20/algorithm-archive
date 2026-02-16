'''
1 안타: 타자와 모든 주자가 한 루씩 진루한다.
2 2루타: 타자와 모든 주자가 두 루씩 진루한다.
3 3루타: 타자와 모든 주자가 세 루씩 진루한다.
4 홈런: 타자와 모든 주자가 홈까지 진루한다.
0 아웃: 모든 주자는 진루하지 못하고, 공격 팀에 아웃이 하나 증가한다.


시작[] ->  1루[] -> 2루[] -> 3루[] ->  홈[]

선수 총 9명
1번 선수는 4번타자 고정
1루->2루->3루->홈에 도착하면 1점

총 N이닝 동안 게임 진행
3아웃이 발생하지 않으면 이닝은 안끝남
= 3아웃이 발생할때까지 1번 타자부터 9번타자까지 계속 돌아가면서 반복

다음 이닝에서 타자가 1번부터 다시 시작하지는 않음 전 이닝에서 이어서 진행


'''
from itertools import permutations

N=int(input())
I=[[0]+list(map(int,input().split())) for _ in range(N)]  #각 선수가 각 이닝에서 얻는 결과 ex)I[1][1] -> 1번 이닝에서 1번 선수가 얻는 결과
mx_score=0

players=[2,3,4,5,6,7,8,9]

for p in permutations(players,8):
    p=list(p)
    p=p[:3]+[1]+p[3:]
    score=0
    idx=0
    for round in range(N):
        out=0
        b1=b2=b3=0
        while out<3:
            player=p[idx]
            
            if I[round][player]==0:
                out+=1
            elif I[round][player]==1:
                score+=b3
                b3=b2
                b2=b1
                b1=1

            elif I[round][player]==2:
                score+=b2+b3
                b3=b1
                b2=1
                b1=0

            elif I[round][player]==3:
                score+=b1+b2+b3
                b3=1
                b2=b1=0

            elif I[round][player]==4:
                score+=b1+b2+b3+1
                b1=b2=b3=0

            idx=(idx+1)%9

    mx_score=max(mx_score,score) 
print(mx_score)
    
            
            
            



