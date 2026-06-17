'''
프로그래머스 12904 가장 긴 팰린드롬

입력:
s

구조:
각각 위치로 확인해서 홀수, 짝수 팰린드롬 보기
가장 긴 길이를 반환하기
'''


def solution(s):
    answer = 1
    n = len(s)

    for i in range(n):
        left = i
        right = i

        while left >= 0 and right < n:

            if s[left] == s[right]:
                cnt = right - left + 1

                if cnt > answer:
                    answer = cnt

                left -= 1
                right += 1


            else:
                break

        left = i
        right = i + 1

        while left >= 0 and right < n:

            if s[left] == s[right]:
                cnt = right - left + 1

                if cnt > answer:
                    answer = cnt

                left -= 1
                right += 1


            else:
                break

    return answer