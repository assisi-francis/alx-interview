#!/usr/bin/python3
"""
Island perimeter computing module
"""


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Start with the full perimeter

                # Check adjacent cells and subtract if they are also land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

    return perimeter
