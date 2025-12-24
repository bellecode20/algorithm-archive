r,c,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]

min_time=0 #최소 시간 담을 변수

#100*100 배열에 맞춰서 더미값 넣기(나중에 배열 바꿔치기 편할라고)
# if len(A)<100:
#     while len(A) !=100:
#         A.append([0])

#     for x in A:
#         if len(x)<100:
#             while len(x) !=100:
#                 x.append(0)

while min_time<=100: #100초까지만 반복
    if r-1 < len(A) and c-1 < len(A[r-1]) and A[r-1][c-1] == k:
        break

    r_count=len(A)
    c_count=max(len(row) for row in A)

    # for i in range(0,100):
    #     for j in range(0,100):
    #         if A[i][j] == 0 and j>r_count:
    #             r_count=j
    #             break
    #     if A[i][0] == 0 and i>c_count:
    #         c_count=i


    
    if r_count>=c_count:#행의 개수가 열의 개수보다 크거나 같은 경우

        c_max=0   #열의 최대길이 초기값
        
        #출현빈도수 카운트
        for i in range(0,len(A)): #행

            #count 초기화
            count=[]
            for k in range(0,101):
                count.append([k,0]) #튜플같은 리스트로 출현빈도 기록할거임(해당숫자,숫자가 출현한 빈도수)

            for j in range(len(A[i])): #열
                if A[i][j]==0:  #0이면 그 뒤는 다 더미값 0이니까 현재 반복문 종료 
                    break
                count[A[i][j]][1]+=1 #현재 위치한 숫자의 출현빈도 카운트 +1

            #튜플 정렬
            count.sort(key=lambda x:(x[1],x[0]))#(출현빈도수 오름차순, 해당숫자 오름차순)


            #현재 행을 초기화
            for x in range(len(A[i])):
                A[i][x]=0


            #현재 행에 다시 값 넣기
            l=0
            for a,b in count:
                if b==0:    #출현빈도수가 0이면 종료(어차피 그 뒤 값도 전부 0임)
                    break
                else:
                    A[i][l]=(a)
                    l+=1
                    A[i][l]=(b)
                    l+=1
                    if l >= 100:
                        break

            #바뀐 행의 열의 최대 길이 찾기
            c_max=max(c_max,len(A[i]))  

        for i in range(len(A)):
            while len(A[i]) < c_max:
                A[i].append(0)


    else:#행의 개수가 열의 개수보다 작은 경우
            

        c_max=0   #열의 최대길이 초기값
        
        #출현빈도수 카운트
        for i in range(0,len(A)): #열

            #count 초기화
            count=[]
            for k in range(0,101):
                count.append([k,0]) #튜플로 출현빈도 기록할거임(해당숫자,숫자가 출현한 빈도수)

            for j in range(len(A)): #행
                if i >= len(A[j]):
                    continue
                if A[j][i]==0:  #0이면 그 뒤는 다 더미값 0이니까 현재 반복문 종료 
                    break
                count[A[j][i]][1]+=1 #현재 위치한 숫자의 출현빈도 카운트 +1

            #튜플 정렬
            count.sort(key=lambda x:(x[1],x[0]))#(출현빈도수 오름차순, 해당숫자 오름차순)

            #현재 열을 초기화
            for arr in A:
                arr[i]=0



            #현재 열에 다시 값 넣기
            
            l=0
            for a,b in count:
                if b==0:    #출현빈도수가 0이면 종료(어차피 그 뒤 값도 전부 0임)
                    break
                else:
                    while len(A) <= l:
                        A.append([0] * c_count)
                    A[l][i]=a
                    l+=1
                    A[l][i]=b
                    l+=1
        for i in range(len(A)):
            A[i] = A[i][:100]

    min_time+=1 #시간 +1초



if min_time>100:
    print(-1)
else:
    print(min_time)


#-------------------------------------

# 어떻게 접근했는지

# 정렬 후 값을 다시 A 배열에 넣는 방식으로 접근
# 없는 인덱스에 값을 넣으면서 `IndexError` 발생.
# 이를 피하려고 배열을 처음부터 100×100으로 만들고 빈칸은 0으로 채움.
# 배열 크기를 고정하면 값 할당이 쉬울 거라 판단

# ---

# 어디서 틀렸는지

# 배열을 100×100으로 고정하니까 실제 행/열 길이 변화를 파악하기 어려워짐.
# 답이 계속 -1이 나옴
# 100×100 구조를 제거하려다 얽힌 코드가 많아 그 코드들을 수정하면서 코드가 복잡해짐

# ---

# 정답 코드 분석

# 배열은 충분히 크게 고정하고 실제 상태는 n, m으로 관리
# 배열 크기를 바꾸지 않고 n, m만 갱신




