x = str(int(input()) * int(input()) * int(input()))
for i in range(10):
    print(x.count(chr(i + ord('0'))))