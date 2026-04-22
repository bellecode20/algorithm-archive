s = input().strip()
bomb = input().strip()
stack = []
m = len(bomb)
# def explode():
#     return

for ch in s:
    stack.append(ch)
    if stack[-1] == bomb[-1] and len(stack) >= m:
        if ''.join(stack[-m:]) == bomb:  
            del stack[-m:]  # stack 뒤에서 m개 원소 한번에 삭제

if stack:
    print(''.join(stack))
else:
    print('FRULA')

'''
del lst[:2]    # 앞에서 2개 삭제
del lst[-2:]   # 뒤에서 2개 삭제
'''