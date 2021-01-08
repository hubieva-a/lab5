n = input("Предложение - ")
commas = n.count(',')
if commas > 0:
    commaindex = n.find(',')
    ncount = n.count('н')
    print(ncount)
else:
    print("Букв н нет")

