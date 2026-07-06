def solution(plans):
    answer = []
    p=[]
    for name, start, playtime in plans:
        h,m=start.split(':')
        time=int(h)*60+int(m)
        p.append((name,time,int(playtime)))
    p.sort(key=lambda x: (x[1]))    #빨리 시작하는 순서로 정렬
    
    stack=[]    #미룬과제들 담을 리스트
    for i in range(len(p)-1):
        name,time,pt=p[i]   #과제이름, 과제시작시간, 과제걸리는시간
        end=time+pt
        
        if end>p[i+1][1]:   #현재과제 진행중에 새과제 시작시간이 된다면
            stack.append([name,pt-(p[i+1][1]-time)]) #과제이름,현재과제남은시간
        else:   #다음과제 전에 현재과제를 끝낼 수 있다면
            answer.append(name)
            if p[i+1][1]>end and stack: #(현재과제 끝나는시간과 다음과제시작시간 사이에 텀이 있고)and(미룬과제가 있을때)
                spare=p[i+1][1]-end #확보할수 있는 여분시간
                while spare and stack:  #여분시간을 다 쓰거나 or 미룬과제를 다할때까지
                    if stack[-1][1]>spare:  #제일최근미룬과제 남은시간>여분시간
                        stack[-1][1]-=spare
                        spare=0
                    else:
                        if stack[-1][1]<spare:  #제일최근미룬과제 남은시간<여분시간
                            spare-=stack[-1][1] 
                        elif stack[-1][1]==spare:   #제일최근미룬과제 남은시간==여분시간
                            spare=0
                        answer.append(stack[-1][0])
                        stack.pop()

    answer.append(p[-1][0])

    if stack:
        for i in range(len(stack)-1,-1,-1):
            answer.append(stack[i][0])
                               
    
    return answer