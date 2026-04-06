def solution_1(book_time):
    answer = 0
    rooms = []
    
    def get_minutes(timestamp):
        hh, mm = map(int, timestamp.split(":"))
        return hh * 60 + mm
    
    book_minutes = []
    for book in book_time:
        start, end = get_minutes(book[0]), get_minutes(book[1])  
        book_minutes.append([start, end])
    
    book_minutes.sort()  # 종료시각이 아닌 시작시각으로 정렬했어야 함

    
    for start, end in book_minutes:
        if not rooms:
            rooms.append(end + 10)
            continue
        
        good_end_time = int(1e9)
        next_room = -1
        
        for i in range(len(rooms)):
            # 제일 빨리 끝나는 시간 찾기
            if rooms[i] <= start and rooms[i] < good_end_time:
                good_end_time = rooms[i]
                next_room = i  # 
        
        if next_room == -1:  # 모든 방이 꽉차있던 경우, 새로운 방에 넣는다. 
            rooms.append(end + 10)
        else:
            rooms[next_room] = end + 10
    
    answer = len(rooms)
        
    return answer



# 우선순위 큐
import heapq

def solution_2(book_time):
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    # 시작 시간 기준 정렬
    books = []
    for start, end in book_time:
        s = to_minutes(start)
        e = to_minutes(end) + 10  # 청소 시간 포함
        books.append((s, e))
    
    books.sort()

    rooms = []  # 각 방의 "다시 사용 가능한 시각" 최소 힙

    for start, end in books:
        # 가장 빨리 비는 방이 현재 시작 시각 이전이면 재사용
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        
        heapq.heappush(rooms, end)

    return len(rooms)

