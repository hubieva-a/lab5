# Дано предложение. Удалить из него все буквы о, стоящие на нечетных местах.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = str(input("Предложение - "))
    m = len(n)
    for i in range(1, m):
        i = str(i)
        if n.find(i) % 2 == 1:
            n = n.replace('о', '')
    print(n)
