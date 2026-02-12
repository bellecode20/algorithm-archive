from itertools import permutations

def rotate(x,y,ss,arr):
  
        temp = arr[x][y]
        
        for k in range(x, x + ss):
            arr[k][y] = arr[k+1][y]
        for k in range(y, y + ss):
            arr[x+ss][k] = arr[x+ss][k+1]
        for k in range(x + ss, x, -1):
            arr[k][y+ss] = arr[k-1][y+ss]
        for k in range(y + ss, y + 1, -1):
            arr[x][k] = arr[x][k-1]

        arr[x][y+1] = temp
    
N, M, K = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
r_info=[list(map(int,input().split())) for _ in range(K)]
mn=float('inf')

for a in permutations(r_info):
    A_copy = [row[:] for row in A]
    for r,c,s in a:
        r,c=r-1,c-1
        for i in range(1,s+1):
            rotate(r-i,c-i,i*2,A_copy)
    mn=min(mn,min(sum(lst) for lst in A_copy))

print(mn)
