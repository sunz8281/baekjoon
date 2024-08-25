
    if i%2==0: turn+=1
    for _ in range(turn):
        num+=1
        x += dx[i]
        y += dy[i]
        if 0>x or 0>y or x2>x or y2>y:
            continue
        arr[y][x] = num