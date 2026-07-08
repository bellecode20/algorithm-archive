'''
프로그래머스 64065 튜플

입력:
s
'''

def solution(s):
    answer = []
    visited = set()
    s = s[2:-2]
    arr = s.split('},{')
    arr.sort(key=lambda x: len(x))

    for temp in arr:
        nums = temp.split(',')


        for num in nums:
            num = int(num)


            if num in visited:
                continue


            visited.add(num)
            answer.append(num)

    return answer