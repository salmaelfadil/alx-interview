#!/usr/env python3
"""island perimeter module"""


def island_perimeter(grid):
    """calculates the perimeter of a grid"""
    perim = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perim += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perim += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perim += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perim += 1
    return perim
