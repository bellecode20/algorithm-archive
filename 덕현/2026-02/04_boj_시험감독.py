'''
시험감독


'''
N = int(input())
room = list(map(int,input().split()))
B, C = map(int,input().split())
cnt = N


for i in range(N):
    if room[i]-B > 0:
        if (room[i]-B)%C==0:
            cnt += ((room[i]-B)//C)
        else:
            cnt += ((room[i]-B)//C) + 1

print(cnt)