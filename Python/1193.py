X = int(input())

# X번째 분수가 속한 대각선 번호를 찾음
line = 1
while X > line:
    X -= line
    line += 1

# 대각선 번호가 홀수일 때는 분자가 감소하고, 분모가 증가함
if line % 2 == 0:
    print(f"{X}/{line + 1 - X}")
else:
    print(f"{line + 1 - X}/{X}")