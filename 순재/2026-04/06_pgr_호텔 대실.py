def solution(book_time):
    def mn(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    time = [0] * 1451

    for start, end in book_time:
        s = mn(start)
        e = mn(end) + 10

        time[s] += 1
        time[e] -= 1

    ans = 0
    cur = 0

    for x in time:
        cur += x
        ans = max(ans, cur)

    return ans