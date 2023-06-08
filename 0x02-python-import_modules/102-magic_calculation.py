#!/usr/bin/python3
def magic_calculation(c, d):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub
    if c < d:
        e = add(c, d)
        for n in range(4, 6):
            e = add(e, n)
            return (e)
        else:
            return sub(c, d))
