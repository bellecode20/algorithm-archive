'''
현재 설치된 기지국 기준으로 왼쪽에 설치해나가기
'''

def solution(n, stations, w):
    answer = 0
    stations_len = len(stations)
    left_idx = 0  # 영향받는 범위 중 제일 왼쪽
    
    
    for i in range(stations_len):
        start_idx = stations[i] - w  # 영향 받음
        
        if start_idx < 0:  # 설치 안해도 되는 경우
            left_idx = stations[i] + w
            continue
        
        rest = (start_idx - left_idx - 1)
        cnt = math.ceil(rest / (w * 2 + 1))
        
        left_idx = min(stations[i] + w, n)
        answer += cnt
    
    if left_idx == n:  # 마지막 기지국 세우고 오른쪽에 남은 아파트 없는 경우
        return answer
    
    # 마지막 기지국 기준 오른쪽 채우기
    rest = (n - left_idx)
    cnt = math.ceil(rest / (w * 2 + 1))
    answer += cnt
    return answer

print(f"답: {solution(11, [4, 11], 1)}\n")
print(f"답: {solution(16, [9], 2)}")



# 다른 풀이
import math
def solution2(n, stations, w):
    answer = 0
    start = 1  # 전파를 확인하기 시작할 아파트 번호
    coverage = 2 * w + 1  # 기지국 하나가 커버하는 총 범위

    for station in stations:
        # 현재 확인하는 위치(start)가 기존 기지국의 전파 왼쪽 범위(station - w)보다 앞에 있다면
        # 그 사이 구간은 전파가 닿지 않는 '빈 구간'입니다.
        if start < station - w:
            end = station - w - 1
            length = end - start + 1  # 빈 구간의 길이
            
            # 필요한 최소 기지국 수를 구해서 더해줌
            answer += math.ceil(length / coverage)
            
        # 다음으로 전파를 확인해야 할 위치는 현재 기지국의 오른쪽 전파 범위를 벗어난 곳
        start = station + w + 1

    # 모든 기존 기지국을 확인한 후, 맨 마지막 기지국 오른쪽에 남은 빈 구간 처리
    if start <= n:
        length = n - start + 1
        answer += math.ceil(length / coverage)

    return answer