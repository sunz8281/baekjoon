s = input()
s = "(" + ")-(".join([("+".join([str(int(j)) for j in i.split("+")])) for i in s.split("-")]) + ")"
print(eval(s))