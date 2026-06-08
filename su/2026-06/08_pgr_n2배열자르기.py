'''
n <= 10^7 이므로 직접 구현시 시간초과 발생하였음
'''

def solution(n, left, right):
    answer = []
    
    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        
        answer.append(max(row, col) + 1)
        
    return answer