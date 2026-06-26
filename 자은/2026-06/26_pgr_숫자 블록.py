def find(n):
    if n==1:return 0

    cand=[1]    #약수에서 1은 항상 잇음
    for e in range(2,int(n**0.5)+1):
        if n%e==0:
            if n//e<=10000000:  #몫이 10000000보다 작으면
                cand.append(n//e)
                break   #종료
            else:
                cand.append(e)
    return max(cand)

def solution(begin, end):
    answer = []
    for s in range(begin,end+1):
        answer.append(find(s))

    return answer