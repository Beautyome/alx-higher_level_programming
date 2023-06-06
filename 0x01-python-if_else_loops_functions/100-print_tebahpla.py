#!/usr/bin/python3
for o in range(122, 96, -2):
    cs = f"{chr(o):s}{chr(o + ord('A') - ord('a') - 1):s}"
    print("{:s}".format(cs), end="")
