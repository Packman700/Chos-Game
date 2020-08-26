def Return_a_b(x1,y1,x2,y2):
    a = (y2-y1)/(x2-x1)
    if x2*a < 0:
        b = y2+(x2 * a)
    else:
        b = y2-(x2 * a)
    return (a,b)

