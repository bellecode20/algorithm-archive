def solution(message, spoiler_ranges):
    answer = 0
    M=message.split()
    word_s_e_index=[]
    idx=0
    important=set() #중복허용하지 않는 스포방지된 단어들
    spoiled=[]  #중복 허용하는 스포방지된 모든 단어들
    for word in M:
        start=message.find(word,idx)
        end=start+len(word)-1
        idx=end+1
        word_s_e_index.append((word,start,end))
    
    for S,E in spoiler_ranges:
        for w,ws,we in word_s_e_index:
            if not (we < S or ws > E):    #단어가 스포방지 범위 안에 있으면
                important.add(w)
                spoiled.append((w,ws,we))
    
    not_important=set() #스포방지된 단어 중 중요하지 않은 단어
    for w,ws,we in word_s_e_index:  #메시지의 모든 단어들을 순회
        if (w,ws,we) in spoiled:  #스포방지된 단어는 제외
            continue
            
        #스포방지가 되지 않은 단어들중에 스포일러된 단어랑 똑같은게 있으면
        if w in important:
            not_important.add(w)    #중요하지 않은 단어에 추가
                
    for word in important:  #스포방지된 단어들을 순회하면서
        if word not in not_important:   #중요하지 않은 단어에 포함이 안된다면
            answer+=1

    return answer