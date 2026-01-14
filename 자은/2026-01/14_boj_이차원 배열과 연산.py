'''
정렬기준
1. 수의 등장 횟수가 커지는 순
2. 수가 커지는 순

-> 배열 A에 정렬된 결과(수+등장횟수)를 넣음
'''

def lst_sort(lst):
    global max_len

    num = set()
    
    #어떤 숫자들이 있는지 확인
    for i in lst:   
        if i == 0:
            continue
        num.add(i)
    
    cnt=[]
    for n in num:
        n_cnt=lst.count(n)
        cnt.append((n_cnt,n))
    cnt.sort()

    new_lst=[]
    for nc,n in cnt:
        new_lst.append(n)
        new_lst.append(nc)
    new_lst = new_lst[:100]
    max_len=max(max_len,len(new_lst))
    return new_lst

r,c,k = map(int,input().split())
A =  [list(map(int,input().split())) for _ in range(3)]
ans=-1
t=0
while t<=100:
    if r-1 < len(A) and c-1<len(A[0]):
        if A[r-1][c-1]==k:
            ans=t
            break
    if t==100:
        break
    t+=1
    max_len=0

    if len(A) >= len(A[0]): #행의 개수 >= 열의 개수
        for i in range(len(A)):
            A[i] = lst_sort(A[i])
        for lst in A:   #더미 0 넣기
            while len(lst)<max_len:
                lst.append(0)

    elif len(A) < len(A[0]):#행의 개수 < 열의 개수
        a=[]
        for j in range(len(A[0])):
            c_lst=[]
            for i in range(len(A)):
                c_lst.append(A[i][j])
            c_lst=lst_sort(c_lst)
            a.append(c_lst)
        for lst in a:
            while len(lst)<max_len:
                lst.append(0)

        A=[[] for _ in range(len(a[0]))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                A[j].append(a[i][j])


print(ans)