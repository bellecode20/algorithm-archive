def solution(m, musicinfos):
    answer = ''
    mx_playing=0
    for info in musicinfos:
        start,end,title,chord =info.split(",")
        s_h,s_m=map(int,start.split(":"))
        e_h,e_m=map(int,end.split(":"))
        playing_time=(e_h*60+e_m)-(s_h*60+s_m)
        new_chord=[]
        new_m=[]
        for i in range(len(chord)):
            if chord[i]=='#':
                new_chord[-1]=chord[i-1]+chord[i]
            else:
                new_chord.append(chord[i])
        for i in range(len(m)):
            if m[i]=='#':
                new_m[-1]=m[i-1]+m[i]
            else:
                new_m.append(m[i])
        playing_chord=[]        
        for i in range(playing_time):
            playing_chord.append(new_chord[i%len(new_chord)])
        
        for i in range(len(playing_chord)-len(new_m)+1):
            lst=playing_chord[i:i+len(new_m)]
            if lst==new_m and mx_playing<playing_time:
                answer=title
                mx_playing=playing_time
    if answer=='':
        return "(None)"
    else:
        return answer