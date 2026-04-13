def solution(picks, data):
    data = data[:sum(picks) * 5]
    group = []

    for i in range(0, len(data), 5):
        chunk = data[i:i+5]

        dia = 0
        iron = 0
        stone = 0

        for m in chunk:
            if m == "diamond":
                dia += 1
                iron += 5
                stone += 25
            elif m == "iron":
                dia += 1
                iron += 1
                stone += 5
            else:
                dia += 1
                iron += 1
                stone += 1

        group.append((dia, iron, stone))

    group.sort(key=lambda x: (-x[2], -x[1], -x[0]))

    dia, iron, stone = picks
    ans = 0

    for d, i, s in group:
        if dia:
            ans += d
            dia -= 1
        elif iron:
            ans += i
            iron -= 1
        else:
            ans += s
            stone -= 1

    return ans