day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = map(int, input().split())
print(day[(sum(date[:m-1]) + d - 1) % 7])