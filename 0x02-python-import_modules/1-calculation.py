#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    c = 10
    d = 5

    print("{} + {} = {}".format(c, d, add(c, d)))
    print("{} - {} = {}".format(c, d, sub(c, d)))
    print("{} * {} = {}".format(c, d, mul(c, d)))
    print("{} / {} = {}".format(c, d, div(c, d)))
