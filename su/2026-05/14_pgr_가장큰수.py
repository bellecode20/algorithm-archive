from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    return 0

def solution(prices):
    answer = []
    prices = list(map(str, prices))
    prices.sort(key=cmp_to_key(compare))
    
    answer = ''.join(prices)
    # 정렬 후 첫번쨰가 0이면 뒤에도 다 0임
    return '0' if answer[0] == '0' else answer