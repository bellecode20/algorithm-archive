'''
프로그래머스 84512 모음사전

구조:
AEIOU 순서
앞자리가 바뀌면 뒤에 올 수 있는 경우를 한 번에 더하기
현재 글자 값 + 1 씩 답에 더하기
'''

def solution(word):
    graph = ['A', 'E', 'I', 'O', 'U']
    cnt = [781, 156, 31, 6, 1]

    ans = 0

    for i in range(len(word)):
        for j in range(5):
            if word[i] == graph[j]:
                ans += cnt[i] * j + 1
                break

    return ans