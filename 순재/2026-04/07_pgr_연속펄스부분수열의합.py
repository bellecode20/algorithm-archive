def solution(seq):
    mx1 = cur1 = seq[0]
    mx2 = cur2 = -seq[0]

    for i in range(1, len(seq)):
        if i % 2 == 0:
            v1 = seq[i]
            v2 = -seq[i]
        else:
            v1 = -seq[i]
            v2 = seq[i]

        cur1 = max(v1, cur1 + v1)
        mx1 = max(mx1, cur1)

        cur2 = max(v2, cur2 + v2)
        mx2 = max(mx2, cur2)

    return max(mx1, mx2)