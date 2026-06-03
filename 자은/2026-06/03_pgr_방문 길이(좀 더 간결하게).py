def solution(dirs):
    path=set()
    nav={'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)}
    x=y=0
    
    for d in dirs:
        nx,ny=x+nav[d][0],y+nav[d][1]
        
        if -5<=nx<=5 and -5<=ny<=5:
            path.add((x,y,nx,ny))
            path.add((nx,ny,x,y))
            x,y=nx,ny
    
    return len(path)//2