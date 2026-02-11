'''
BOJ 17406 배열 돌리기 4

입력:
N, M, K
A
연산 K개

구조:
순열짜끼
돌리기 배열
최솟값 계속 마들긴
'''

from itertools import permutations
import copy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ops = []
for _ in range(K):
    r, c, s = map(int, input().split())
    ops.append((r -1, c -1, s))


def rotate(arr, r, c,s):
    for d in range(1, s + 1):
        top = r -d
        left = c - d
        bottom = r + d
        right = c+ d

        prev = arr[top][left]

        for j in range(left + 1, right+1):
            arr[top][j], prev = prev, arr[top][j]

        for i in range(top +1, bottom+1):
            arr[i][right], prev = prev, arr[i][right]

        for j in range(right -1, left-1, -1):
            arr[bottom][j], prev = prev, arr[bottom][j]

        for i in range(bottom -1, top-1, -1):
            arr[i][left], prev = prev, arr[i][left]


ans = float('inf')

for order in permutations(range(K)):
    arr = copy.deepcopy(A)

    for idx in order:
        r, c, s = ops[idx]
        rotate(arr, r, c, s)

    for i in range(N):
        row_sum = sum(arr[i])
        if row_sum < ans:
            ans = row_sum

print(ans)
