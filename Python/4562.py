for l in [*open(0)][1:]:
    a, b = l.split()
    print(("NO" if a<b else "MMM") + " BRAINS")