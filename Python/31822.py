c=input()[:5]
print(len(list(filter(lambda x:x[:5]==c,[input()for _ in range(int(input()))]))))