from itertools import product

def find_five(lst,r):
    left=-1
    for i in range(N):
        if lst[i]:
            left=i
            break
    for c in range(left+1,N):
        if lst[c]:
            break
        visited[r][c]=5

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
answer=(N**2)*100

for x,y in product(range(N-2),range(1,N-1)):
    for d1,d2 in product(range(1,y+1),range(1,N-y)):
        if x+d1+d2>=N or y+d2>N: continue

        visited=[[0]*N for _ in range(N)]
        people=[0,0,0,0,0]  #1~5번구역 인원수

        #1,4 경계선
        for i in range(d1+1):
            visited[x+i][y-i]=5
            visited[x+d2+i][y+d2-i]=5

        #2,3 경계선
        for i in range(d2+1):
            visited[x+i][y+i]=5
            visited[x+d1+i][y-d1+i]=5
        
        #5번구역 찾기
        for i in range(x+1,x+d1+d2):
            find_five(visited[i],i)
        
        for r in range(N):
            for c in range(N):
                if visited[r][c]==5:
                    people[4]+=arr[r][c]
                    continue
                if r<x+d1 and c<=y:
                    people[0]+=arr[r][c]
                if r<=x+d2 and y<c<=N:
                    people[1]+=arr[r][c]
                if x+d1<=r and c<y-d1+d2:
                    people[2]+=arr[r][c]
                if x+d2<r and y-d1+d2<=c:
                    people[3]+=arr[r][c]

        answer=min(answer,max(people)-min(people))

print(answer)
