from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def diff(a, b):
        return sum(c1 != c2 for c1, c2 in zip(a, b))
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for w in words:
            if w not in visited and diff(word, w) == 1:
                visited.add(w)
                queue.append((w, count + 1))
    
    return 0