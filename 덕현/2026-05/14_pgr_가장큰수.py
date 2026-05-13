'''
프로그래머스 42746 가장 큰 수

입력:
numbers

구조:
숫자 -> 문자열
문자열을 4번 반복한 값 기준으로 정렬
0000인 경우에만 0하면 될듯
'''

def solution(numbers):
    arr = []

    for num in numbers:
        arr.append(str(num))

    arr.sort(key=lambda x: x * 4, reverse=True)

    ans = ''

    for num in arr:
        ans += num

    if ans[0] == '0':
        return '0'

    return ans