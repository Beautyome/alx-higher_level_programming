#!/usr/bin/python3
a = 1
while a < 100:
    if a % 10 == 0:
        a = int(a + (a / 10) + 1)
        continue
    print("{:02d}".format(a), end=", " if a < 89 else "\n")
    a += 1
