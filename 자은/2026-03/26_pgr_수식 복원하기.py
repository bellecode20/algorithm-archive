def change_10(a,b,c,op,n):  #n진법을 10진법으로
    
    try:
        ch_a=int(a,n)
        ch_b=int(b,n)
        ch_c=int(c,n)
    except ValueError:
        return False

    if op=='+':
        return ch_a+ch_b==ch_c
    elif op=='-':
        return ch_a-ch_b==ch_c


def change(c,n):    #10진법을 n진법으로
    if c==0:
        return 0
    changed=''
    
    while c>0:
        changed=str(c%n)+changed
        c//=n
    return int(changed)

def solution(expressions):
    answer = []
    finds={2,3,4,5,6,7,8,9} #수식들에서 사용된 진법으로 추측되는 것
    guess_ex=[] #답을 추측해야하는 수식들
    for ex in expressions:
        a,op,b,eq,c=ex.split()
        
        if c == 'X':
            nums = a + b
        else:
            nums = a + b + c
        max_digit = max(int(d) for d in nums)   #a,b,c중에 최대값
        finds = {i for i in finds if i > max_digit} #finds에 담긴 것 중에서 max_digit보다 큰 숫자만 담음(예) 2진법의 수식에서는 숫자 2 이상이 나올 수 없음)

        if c=='X':  #답을 추측해야하는 수식들은 guess_ex에 담아두기
            guess_ex.append((a,op,b))
        else:

            find=set()  #해당 수식에서 사용된 진법으로 추측되는 것
            
            for i in range(2,10):
                if change_10(a,b,c,op,i):
                    find.add(i)
            if find :
                finds&=find

    for a,op,b in guess_ex: #추측해야하는 수식들의 답 찾기
        result=set()    #추측되는 답들
        
        for i in finds:
            try:
                ch_a,ch_b=int(a,i),int(b,i)
            except ValueError:
                continue
            ch_c=0
            
            if op=='+':
                ch_c=ch_a+ch_b
            elif op=='-':
                ch_c=ch_a-ch_b
            
            result.add(change(ch_c,i))
            
        
        if len(result)==1:
            c=list(result)[0]
            answer.append(f"{a} {op} {b} = {c}")
        else:
            answer.append(f"{a} {op} {b} = ?")
    
    return answer