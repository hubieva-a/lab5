s = input("Sentence - ")
ocount = s.count('o')
acount = s.count('a')
if ocount > acount:
    print("There's more o's")
else:
    print("There's more a's")