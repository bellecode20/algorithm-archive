'''
프로그래머스 68936 쿼드압축 후 개수 세기

입력:
arr

구조:
dfs로 나눠서 풀기
전부 같으면 answer
다르면 4개 나누기
'''
def solution(arr):
    answer = [0, 0]
    n = len(arr)

    dfs(arr, answer, 0, 0, n)

    return answer

def dfs(arr, answer, r, c, size):
    num = arr[r][c]

    for i in range(r, r + size):
        for j in range(c, c + size):
            if arr[i][j] != num:
                half = size // 2

                dfs(arr, answer, r, c, half)
                dfs(arr, answer, r, c + half, half)
                dfs(arr, answer, r + half, c, half)
                dfs(arr, answer, r + half, c + half, half)

                return

    answer[num] += 1


