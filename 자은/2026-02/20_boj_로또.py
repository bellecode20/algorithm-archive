from itertools import combinations

while True:
    lst=list(map(int,input().split()))
    if lst[0]==0:break
    k=lst[0]
    lst=lst[1:]

    for c in combinations(lst,6):
        print(*c)
    print()