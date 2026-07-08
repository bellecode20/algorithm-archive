'''
길이로 정렬:    arr.sort(key=lambda x: len(x))

'''

def solution(s):
    answer = []
    sorted_s = []
    i = 1
    
    while i < len(s) - 1:
        temp = [0, set()]
        
        if s[i] == "{":
            nxt_i = i + 1

            while s[nxt_i] != "}":
                nxt_i += 1

            temp[0] = nxt_i - i - 1
            temp[1] = set(map(int, s[i+1:nxt_i].split(",")))
            i = nxt_i + 1
            
        else:
            i += 1
            continue

        sorted_s.append(temp)
        
    sorted_s.sort()

    for i in range(len(sorted_s)):
        _, tp = sorted_s[i]
        if i == 0:
            answer.append(list(tp)[0])
            continue
        
        added = tp - sorted_s[i - 1][1]
        answer.append(added.pop())

    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{20,111},{111}}"))