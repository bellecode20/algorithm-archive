N = int(input())
T=[0]*N
P=[0]*N
for i in range(N):
    T[i], P[i]= map(int,input().split())

money_sum=[0]*(N+1)

for i in range(N-1,-1,-1):  #뒤에서부터 최대비용찾아가기
    #상담이 가능할때
    if i+T[i]<=N:
        money_sum[i]=max(money_sum[i+1], P[i]+money_sum[i+T[i]])    #상담을 했을때와 안했을때 비교해서 큰 값으로
    #기간을 넘어서서 상담이 불가능할때
    else:
        money_sum[i]=money_sum[i+1]

print(money_sum[0])