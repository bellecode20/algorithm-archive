# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 양의 정수 K가 주어진다.
# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은
# 가장 긴 연속 문자열의 길이를 구한다.
from collections import defaultdict

def find_string(K, W):
    minval, maxval = len(W) + 1, -1
    info = defaultdict(list)
    for i in range(len(W)):
        info[W[i]].append(i)
    
    for idx_list in info.values():
        if len(idx_list) < K:
            continue
        for i in range(len(idx_list) - K + 1):
            minval = min(minval, idx_list[i + K - 1] - idx_list[i] + 1)
            maxval = max(maxval, idx_list[i + K - 1] - idx_list[i] + 1)

    return minval, maxval

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    minval, maxval = find_string(K, W)
    if maxval == -1:
        print(maxval)
    else:
        print(minval, maxval)
    

# 문자를 K개 포함하는 가장 짧은 연속 문자열의 길이
# 