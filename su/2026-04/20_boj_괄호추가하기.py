'''
중첩된 괄호는 사용할 수 없다.
시간초과가 나려나 dfs bfs
연산자 우선순위는 동일하기 때문에, 수식을 계산할 때는 왼쪽에서 순서대로 계산한다.
'''

N = int(input())
expression = list(input().strip())
answer = -int(1e9)

def calc(a, op, b):  
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else: 
        return a * b

def dfs(i, result):  
    global answer
    if i >= N:
        answer = max(answer, result)
        return
    
    # 괄호 안 치는 경우
    no_bracket = calc(result, expression[i], expression[i+1])  
    dfs(i + 2, no_bracket)

    # 괄호를 치는 경우
    if i + 3 < N:
        yes_bracket = calc(expression[i+1], expression[i+2], expression[i+3])
        dfs(i + 4, calc(result, expression[i], yes_bracket))
    
    
dfs(1, expression[0])
print(answer)