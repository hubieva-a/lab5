# Дано предложение. Определить, какая из букв – о или а – встречается
# в нем чаще (принять, что указанные буквы в строке есть).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Sentence - ")
    ocount = s.count('o')
    acount = s.count('a')
    if ocount > acount:
        print("There's more o's")
    else:
        print("There's more a's")