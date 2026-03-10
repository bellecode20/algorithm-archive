from itertools import product

def solution(word):
    l1 = []
    words = ['A','E','I','O','U']
    for i in range(1, 6):
        for j in list(product(words, repeat=i)):  # 단어의 길이가 1인 것부터 5인 것까지 모두 만들기
            l1.append(''.join(j))  # 단어 튜플을 문자열로 변환, 넣기
            
    l1.sort()
    return l1.index(word)+1  # 해당 문자열 위치 찾기