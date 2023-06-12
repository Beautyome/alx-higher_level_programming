#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        k = 0
        for j in range(len(a)):
            print("{:d}".format(a[j]), end=" " if j < len(a) - 1 else "\n")
            k += 1

    if len(matrix[0]) == 0:
        print("{}".format(""))
