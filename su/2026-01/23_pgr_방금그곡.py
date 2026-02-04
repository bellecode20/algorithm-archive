# 방금 그 곡 https://school.programmers.co.kr/learn/courses/30/lessons/17683


def to_minutes(times):
    minutes = 0
    li = times.split(":")
    for i in range(2):
        if i == 0:
            minutes += int(li[i]) * 60
        else:
            minutes += int(li[i])
    return minutes

def del_char(s):
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i + 1] == "#":
            result.append(s[i].lower())
            i += 2
        else:
            result.append(s[i])
            i += 1

    return "".join(result)

def solution(m, musicinfos):
    answer = ''
    m = del_char(m)
    candidates = []
    for i in range(len(musicinfos)):
        st, et, title, music = musicinfos[i].split(",")
        music = del_char(music)
        n = len(music)
        play_time = to_minutes(et) - to_minutes(st)

        # 총 문자열 만들기
        new_music = ""
        new_music += music * (play_time // n) + music[:(play_time % n)]
        
        # 조건을 만족하는 곡
        if m in new_music:
            candidates.append((-play_time, i, title))

    if not candidates:
        return "(None)"
    candidates.sort()
    answer = candidates[0][2]
    
    return answer

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])

# 주의
# 1️⃣ 문자열은 수정 불가능(immutable)
#    → string[i] = ... 처럼 직접 바꾸려고 하면 에러
#    → 항상 "새 문자열"을 만들어서 처리해야 함

# 2️⃣ '#' 처리할 때 이전 문자(string[i-1])를 고치려 하지 말 것
#    → 다음 문자가 '#'인지 확인해서
#    → 하나의 문자로 치환해서 result에 추가하는 방식이 안전함

# 3️⃣ 기억한 멜로디 m은 한 번만 변환해야 함
#    → for문 안에서 매번 del_char(m) 하면 논리적으로 이상해질 수 있음

# 4️⃣ 재생된 멜로디를 만들 때
#    → 비교 대상은 원본 악보 길이(n)가 아니라
#    → 실제 재생된 문자열(new_music)

# 5️⃣ 슬라이딩 범위 실수
#    → range(0, n - target_len) ❌
#    → range(0, len(new_music) - target_len + 1) ⭕

# 6️⃣ 그런데 사실 굳이 직접 슬라이딩 비교할 필요 없음
#    → if m in new_music: 이 한 줄이 더 안전하고 간단

# 7️⃣ candidates 리스트를 for문 안에서 생성함 (생성 시점)
#    → 곡마다 초기화돼서 이전 후보가 전부 사라짐
#    → solution 시작 부분에 한 번만 만들어야 함

# 8️⃣ list.append는 인자를 하나만 받음
#    → append(a, b, c) ❌
#    → append((a, b, c)) ⭕

# 9️⃣ candidates 출력/처리는
#    → 모든 곡을 검사한 뒤에 해야 의미 있음

# 10️⃣ 조건을 만족하는 곡이 없을 경우 "(None)" 반환하는 분기 필요
