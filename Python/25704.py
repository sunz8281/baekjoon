n = int(input())
p = int(input())
if n>=20: x = min(p*75//100, p-2000)
elif n>=15: x = min(p*90//100, p-2000)
elif n>=10: x = min(p*90//100, p-500)
elif n>=5: x = p-500
else: x = p
print(max(0, x))