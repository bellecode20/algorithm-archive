def solution(book_time):
    answer = 0
    room=[]
    for i in range(len(book_time)):
        start,end=book_time[i]
        s_h,s_m=map(int,start.split(":"))
        e_h,e_m=map(int,end.split(":"))
        if e_m>=50:
            e_h+=1
            e_m+=10-60
        else:
            e_m+=10
        book_time[i]=(s_h,s_m,e_h,e_m)
    book_time.sort()
    room.append((book_time[0][2],book_time[0][3]))
    
    for i in range(1,len(book_time)):
        
        sh,sm,eh,em=book_time[i]
        room_add=True
        for j in range(len(room)):
            rh,rm=room[j]
            if sh>rh or (sh==rh and sm>=rm):
                room[j]=(eh,em)
                room_add=False
                break
        if room_add:
                room.append((eh,em))
    answer=len(room)
            
    return answer