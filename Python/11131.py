for l in [*open(0)][2::2]:
    w = sum(map(int, l.split()))
    print('Left' if w<0 else 'Right' if w>0 else 'Equilibrium')