x, y = map(int, input().split())
lst = [0] * (y - x + 1)
i = 2
square = i*i

while square <= y:
    j = x + (square - ((x-1)%square+1))
    while j <= y:
        lst[j-x] = 1
        j += square
    i+=1
    square = i**2

print(lst.count(0))