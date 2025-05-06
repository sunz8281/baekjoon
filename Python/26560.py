for l in [*open(0)][1:]:
    print(l[:-1] + ('' if l[-2] == '.' else '.'))