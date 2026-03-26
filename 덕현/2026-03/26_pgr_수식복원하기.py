'''
프로그래머스 340210 수식 복원하기

입력:
expressions

구조:
가능한 진법 후보 찾기
X가 없는 식으로 진법 거르기
X가 있는 식은 후보 진법마다 계산
결과가 같으면 값 넣기
다르면 ? 넣기
'''


def solution(expressions):
    min_base = 2

    for exp in expressions:
        arr = exp.split()

        for i in range(len(arr[0])):
            cur = int(arr[0][i]) + 1
            if min_base < cur:
                min_base = cur

        for i in range(len(arr[2])):
            cur = int(arr[2][i]) + 1
            if min_base < cur:
                min_base = cur

        if arr[4] != 'X':
            for i in range(len(arr[4])):
                cur = int(arr[4][i]) + 1
                if min_base < cur:
                    min_base = cur

    bases = []

    for base in range(min_base, 10):
        ok = True

        for exp in expressions:
            arr = exp.split()

            if arr[4] == 'X':
                continue

            a = 0
            for i in range(len(arr[0])):
                a = a * base + int(arr[0][i])

            b = 0
            for i in range(len(arr[2])):
                b = b * base + int(arr[2][i])

            c = 0
            for i in range(len(arr[4])):
                c = c * base + int(arr[4][i])

            if arr[1] == '+':
                if a + b != c:
                    ok = False
                    break
            else:
                if a - b != c:
                    ok = False
                    break

        if ok:
            bases.append(base)

    answer = []

    for exp in expressions:
        arr = exp.split()

        if arr[4] != 'X':
            continue

        res = []

        for base in bases:
            a = 0
            for i in range(len(arr[0])):
                a = a * base + int(arr[0][i])

            b = 0
            for i in range(len(arr[2])):
                b = b * base + int(arr[2][i])

            if arr[1] == '+':
                val = a + b
            else:
                val = a - b

            if val == 0:
                s = '0'
            else:
                tmp = []
                while val > 0:
                    tmp.append(str(val % base))
                    val //= base

                tmp.reverse()

                s = ''
                for i in range(len(tmp)):
                    s += tmp[i]

            res.append(s)

        first = res[0]
        same = True

        for i in range(1, len(res)):
            if res[i] != first:
                same = False
                break

        if same:
            answer.append(arr[0] + ' ' + arr[1] + ' ' + arr[2] + ' = ' + first)
        else:
            answer.append(arr[0] + ' ' + arr[1] + ' ' + arr[2] + ' = ?')

    return answer
