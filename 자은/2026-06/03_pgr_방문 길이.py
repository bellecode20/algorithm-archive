def solution(dirs):
    path=set()
    x=y=0
    
    for d in dirs:
        if d=='U':
            if x<5:
                path.add((x,y,x+1,y))
                path.add((x+1,y,x,y))
                x+=1
        elif d=='D':
            if x>-5:
                path.add((x,y,x-1,y))
                path.add((x-1,y,x,y))
                x-=1
        elif d=='R':
            if y<5:
                path.add((x,y,x,y+1))
                path.add((x,y+1,x,y))
                y+=1
        elif d=='L':
            if y>-5:
                path.add((x,y,x,y-1))
                path.add((x,y-1,x,y))
                y-=1
    
    return len(path)//2