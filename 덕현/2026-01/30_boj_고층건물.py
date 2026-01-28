'''
BOJ 1027 고층 건물

입력:
N
H

구조:
- i 에다가 오른쪽 가고 기울기 더 커지면 보인다
- i 왼쪽 기울기 작아지면
'''

N = int(input())
H = list(map(int, input().split()))

ans = 0


for i in range(N):



    cnt = 0
    max_num = None
    max_den = None

    for j in range(i + 1, N):
        num = H[j] - H[i]
        den = j - i

        if max_num is None:
            cnt += 1
            max_num, max_den = num, den
        else:
            if num * max_den > max_num * den:
                cnt += 1
                max_num, max_den = num, den


    min_num = None
    min_den = None

    for j in range(i - 1, -1, -1):
        num = H[j] - H[i]
        den = j - i

        if min_num is None:
            cnt += 1
            min_num, min_den = num, den
        else:
            if num * min_den < min_num * den:
                cnt += 1
                min_num, min_den = num, den

    if cnt > ans:
        ans = cnt

print(ans)
