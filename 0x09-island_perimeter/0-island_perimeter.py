#!/usr/bin/python3
"""Calculate and return the perimeter of an island in the grid."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D list representing the grid where 1
                                    represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                # Check adjacent cells and subtract perimeter for shared sides
                if i > 0 and grid[i - 1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                    perimeter -= 2
    return perimeter
