#!/usr/bin/python3
"""module documentation"""


def pascal_triangle(n):
    """creates a pascal triangle"""
    if n <= 0:
        return []
    vals = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = vals[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        vals.append(row)

    return vals
