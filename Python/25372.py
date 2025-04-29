# for _ in range(int(input())):
#     print("yneos"[0 if 6<=len(input())<=9 else 1::2])
for l in [*open(0)][1:]:
    print("yneos"[0 if 6<=len(l)-1<=9 else 1::2])