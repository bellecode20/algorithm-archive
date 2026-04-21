'''
BOJ 9935 문자열 폭발

입력:
s
bomb
stack
m



구조:
스택으로 하고 마지막이 폭발이면 없애기
없으면 flura출력
'''

s = input()
bomb = input()

stack = []
m = len(bomb)

for ch in s:
    stack.append(ch)

    if len(stack) >= m:
        ok = 1

        for i in range(m):
            if stack[len(stack) - m + i] != bomb[i]:
                ok = 0
                break

        if ok == 1:
            for i in range(m):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))