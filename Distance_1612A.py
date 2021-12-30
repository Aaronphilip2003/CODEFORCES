testcases = int(input())
while testcases!=0:
    a, b = 0, 0
    Bx, By = input().split()
    Bx, By = int(Bx), int(By)
    Cx, Cy = 0, 0
 
    if (Bx+By)%2==0:
        if Bx%2!=0 and By%2!=0:
            if Bx>By:
                Cx = (Bx+By)//2
                Cy = 0
            else:
                Cx = 0
                Cy = (By+Bx)//2
        else:
            Cx = Bx//2
            Cy = By//2
    else:
        Cx, Cy = -1, -1
 
    print(Cx,Cy)
    testcases -= 1
