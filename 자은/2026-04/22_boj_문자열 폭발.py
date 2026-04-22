S=input()
B=input()

stack=[]

for s in S:
    stack.append(s)

    if stack[-len(B):]==list(B):
        del stack[-len(B):]

ans=''.join(stack)
if ans:print(ans)
else:print('FRULA')