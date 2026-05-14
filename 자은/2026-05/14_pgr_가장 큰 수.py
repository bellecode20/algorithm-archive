def solution(numbers):
    numbers.sort(reverse=True,key=lambda x:str(x)*3)
    if numbers[0]==0:return '0'
    answer=''.join(map(str,numbers))
    return answer