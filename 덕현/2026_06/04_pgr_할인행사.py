'''
프로그래머스 131127 할인 행사

입력:
want number discount

구조:
딕셔너리 구조로 10일 세기
기간 상품 세고 같으면 answer+1
'''


def solution(want, number, discount):
    answer = 0
    need = {}
    for i in range(len(want)):
        need[want[i]] = number[i]

    for i in range(0, len(discount) - 9):
        temp = {}
        for j in range(i, i + 10):
            name = discount[j]

            if name in temp:
                temp[name] += 1
            else:
                temp[name] = 1

        flag = True
        for name in need:
            if name not in temp:
                flag = False
                break

            if need[name] != temp[name]:
                flag = False
                break

        if flag == True:
            answer += 1

    return answer