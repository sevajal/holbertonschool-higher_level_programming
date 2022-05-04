#!/usr/bin/python3
for i in range(00, 100):
    x = i / 10
    y = i % 10
    if x < y:
        if i == 89:
            print(f"{i}")
        else:
            print(f"{i:02d}", end=', ')
