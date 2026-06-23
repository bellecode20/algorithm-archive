'''
O(n), 구간, -> 투포인터
투포인터: 
- 양끝에서 마주보면서 오는 방법 (보통 정렬해야하는 경우, 팰린드롬) 
  구명보트[https://school.programmers.co.kr/learn/courses/30/lessons/42885]

- 같은 방향으로 가는 방법
while문 조건을 left <= right 로만 넣으면 배열 끝에 있는 원소는 확인 못하고 중간에 끝나는 경우 발생
right를 n번씩 계속 늘리면서, 만약 늘리는 중에 문제 조건만족하는 경우 left 당겨서 최소길이 계속 갱신하기
'''

from collections import defaultdict

def solution(gems):
    # 1. 전체 보석 종류의 개수 구하기
    total_kinds = len(set(gems))
    
    # 2. 변수
    gem_dict = defaultdict(int)
    left = 0
    min_length = float('inf')
    answer = [1, len(gems)] # 기본값으로 전체 구간 설정
    
    # 3. right를 한 칸씩 이동하며 탐색 (같은 방향 투 포인터)
    for right in range(len(gems)):
        # 우측 확장: 새로운 보석을 딕셔너리에 추가
        gem_dict[gems[right]] += 1
        
        # 좌측 축소: 모든 종류의 보석을 다 포함하고 있는 동안 left를 당김
        while len(gem_dict) == total_kinds:
            current_length = right - left + 1
            
            # 최단 길이 갱신
            if current_length < min_length:
                min_length = current_length
                answer = [left + 1, right + 1] # 문제 조건에 맞게 1번 인덱스로 저장
            
            # left가 가리키던 보석을 하나 뺌
            gem_dict[gems[left]] -= 1
            
            # 개수가 0개가 되면 종류 자체를 제거해야 len(gem_dict)가 줄어듦
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
                
            # left 전진
            left += 1
            
    return answer
