def solution(n, bans):
    ans = ''

    alpha='abcdefghijklmnopqrstuvwxyz'
    al={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

    if bans:
        bans.sort(key=lambda x: (len(x),x)) #길이순,사전순으로 정렬
        for ban in bans:    #문자열주문을 숫자로 변환
            trans=0
            num=1
            for i in range(len(ban)-1,-1,-1):
                trans+=al[ban[i]]*num
                num*=26
            if trans >n:break   #찾아야하는 주문보다 뒷순서면 종료
            else:n+=1
        
    while n>0: #숫자target을 문자열주문으로 변환
        
        rest=n%26  #26으로 나눈 나머지
        share=n//26
        if rest==0:
            rest=26
            share-=1
        ans=alpha[rest-1]+ans
        n=share
    
    return ans