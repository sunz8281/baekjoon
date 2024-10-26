a, b, v = map(int, input().split())
count = (v-b)/(a-b)
if count != int(count): count += 1
print(int(count))