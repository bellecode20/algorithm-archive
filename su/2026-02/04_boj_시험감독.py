# https://www.acmicpc.net/problem/13458


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for i in range(len(A)):
    A[i] -= B
    answer += 1
    
    if A[i] < 0:
        A[i] = 0
    
    answer += (A[i] // C)
    A[i] = A[i] % C

    if A[i] > 0:
        answer += 1

print(answer)
    