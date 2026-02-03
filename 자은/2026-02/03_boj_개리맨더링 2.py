'''
87퍼에서 틀려서 원인 찾는중..
'''

from itertools import product

def cnt_five():
    for i in range(N):
        for j in range(N):
            if five[i][j]:people_cnt[5]+=people[i][j]

def find_five():
    for i in range(N):
        left=right=-1
        for j in range(N):
            if five[i][j]:
                if left>=0:
                    right=j
                    break
                else:left=j
        if left>=0 and right>=0:
            for k in range(left+1,right):
                five[i][k]=5

N=int(input())
people = [list(map(int,input().split())) for _ in range(N)]
min_result=100*(N**2)

for x,y in product(range(N-2),range(1,N-1)):
    for d1, d2 in product(range(1,y+1), range(1,N-y)):
        if x+d1+d2>N-1:continue
        
        people_cnt=[0]*6    #0번인덱스는 더미
        five=[[0]*N for _ in range(N)]

        for i in range(d1+1):
            five[x+i][y-i]=5    #1번경계선
            five[x+d2+i][y+d2-i]=5  #4번경계선

        for j in range(d2+1):
            five[x+j][y+j]=5
            five[x+d1+j][y-d1+j]=5

        find_five()
        cnt_five()
        
        for r in range(N):
            for c in range(N):
                if not five[r][c]:
                    if 0<=r<x+d1 and 0<=c<=y:
                        people_cnt[1]+=people[r][c]
                    elif 0<=r<=x+d2 and y<c<N:
                        people_cnt[2]+=people[r][c]
                    elif x+d1<=r<N and 0<=c<y-d1+d2:
                        people_cnt[3]+=people[r][c]
                    elif x+d2<r<N and y-d1+d2<=c<N:
                        people_cnt[4]+=people[r][c]
        min_result=min(min_result,max(people_cnt[1:])-min(people_cnt[1:]))
print(min_result)
