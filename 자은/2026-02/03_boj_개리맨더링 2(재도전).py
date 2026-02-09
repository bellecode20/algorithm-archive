'''
87퍼에서 틀려서 원인 찾는중..
'''

from itertools import product

def cnt_five():
    for i in range(N):
        for j in range(N):
            if five[i][j]:people_cnt[5]+=people[i][j]   #5번구역이라면 5번인덱스에 인구수 더하기

def find_five():
    for i in range(N):  #각 행마다 안쪽 5번구역 찾기
        left=right=-1   #초기값 -1설정
        for j in range(N):
            if five[i][j]:  #5번구역 시작점 or 끝점 찾기
                if left>=0: #시작점을 이미 찾았다면
                    right=j #끝점찾기
                    break
                else:left=j #시작점찾기
        if left>=0 and right>=0:    #시작점과 끝점을 다 찾았다면
            for k in range(left+1,right):five[i][k]=5   #경계선 안쪽 구역 체크

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
            five[x+j][y+j]=5    #2번경계선
            five[x+d1+j][y-d1+j]=5  #3번경계선

        find_five() #경계선 안쪽 5번구역찾기
        cnt_five()  #5번구역 인구수 세기
        
        for r in range(x + d1):
            for c in range(y + 1):
                if five[r][c]: break
                people_cnt[1] += people[r][c]

        for r in range(x + d2 + 1):
            for c in range(N - 1, y, -1):
                if five[r][c]: break
                people_cnt[2] += people[r][c]

        for r in range(x + d1, N):
            for c in range(y - d1 + d2):
                if five[r][c]: break
                people_cnt[3] += people[r][c]

        for r in range(x + d2 + 1, N):
            for c in range(N - 1, y - d1 + d2 - 1, -1):
                if five[r][c]: break
                people_cnt[4] += people[r][c]


        min_result=min(min_result,max(people_cnt[1:])-min(people_cnt[1:]))  #최소결과값 찾기
print(min_result)
