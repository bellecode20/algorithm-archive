n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mx = -float('inf')
mn = float('inf')

def dfs(i, val, add, sub, mul, div):
    global mx, mn
    
    if i == n:
        mx = max(mx, val)
        mn = min(mn, val)
        return
    
    if add > 0:
        dfs(i+1, val + data[i], add-1, sub, mul, div)
    if sub > 0:
        dfs(i+1, val - data[i], add, sub-1, mul, div)
    if mul > 0:
        dfs(i+1, val * data[i], add, sub, mul-1, div)
    if div > 0:
        if val < 0:
            dfs(i+1, -(-val // data[i]), add, sub, mul, div-1)
        else:
            dfs(i+1, val // data[i], add, sub, mul, div-1)

dfs(1, data[0], add, sub, mul, div)
print(mx)
print(mn)
