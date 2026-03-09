def solution(message, spoiler_ranges):
    answer = 0

    words = []
    idx = 0
    for word in message.split():
        start = message.find(word, idx)  # 해당 단어 나오는 위치(인덱스)를 찾기 (문자열의 idx번째 문자부터 찾는다.)
        end = start + len(word) - 1
        idx = end + 1
        words.append((word, start, end))

    spoiled_words = set()
    normal_words = set()

    for word, ws, we in words:
        is_spoiled = False

        for s, e in spoiler_ranges:
            if we >= s and ws <= e:
                is_spoiled = True
                break

        if is_spoiled:
            spoiled_words.add(word)
        else:
            normal_words.add(word)

    answer = len(spoiled_words - normal_words)
    return answer