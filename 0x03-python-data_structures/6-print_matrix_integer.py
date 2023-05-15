#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, n in enumerate(row):
            print("{:d}".format(n), end="")
            if (index < len(row) - 1):
                print("{}".format(" "), end="")
        print()
