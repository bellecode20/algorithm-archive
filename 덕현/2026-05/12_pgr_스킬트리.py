'''
프로그래머스 스킬트리

입력:
skill
skill_trees

구조:
스킬트리 하나씩 보면서 먼저 뽑은게 있나?
순서보고 앞이랑 같으면 정답 +1
'''

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        arr = []

        for ch in tree:
            if ch in skill:
                arr.append(ch)
        ok = 1
        for i in range(len(arr)):
            if arr[i] != skill[i]:
                ok = 0
                break
        if ok:
            answer += 1

    return answer
