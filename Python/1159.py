n = int(input())
lst = [0]*26
for _ in range(n):
    x = input()
    lst[ord(x[0])-ord('a')] += 1

lst = [chr(i+ord('a')) for i in range(26) if lst[i]>=5]
if len(lst)>0:
    print("".join(lst))
    # print(lst)

else:
    print("PREDAJA")