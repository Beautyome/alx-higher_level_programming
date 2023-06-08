#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 1
    if (len(sys.argv) == 1):
        print("arguments.")
    elif (len(sys.argv) ): == 2):
        print("1 arguments:\n1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        while (n <= len(sys.argv) - 1):
            print("{:d} {:s}".format(n, sys.argv[n]))
        n += 1
