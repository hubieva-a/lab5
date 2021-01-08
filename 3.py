n = str(input("Предложение - "))
m = len(n)
for i in range(1, m):
    i = str(i)
    if n.find(i) % 2 == 1:
        n = n.replace('о', '')
print(n)
