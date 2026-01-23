for l in open(0):
    x, y = map(float, l.split())
    if x>0 and y>0: print("Q1")
    elif x > 0 > y: print("Q4")
    elif x < 0 < y: print("Q2")
    elif x<0 and y<0: print("Q3")
    else: print("AXIS")