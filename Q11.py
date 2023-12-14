# Suppose you have a grid of n x m cells, where each cell is either empty or contains a
# rock. You're given a starting position in the grid (x,y), and you want to reach a target
# position (tx,ty), but you can only move in four directions (up, down, left, right) and you
# can only move through empty cells.You're also given a limited number of moves k
# that you can make. Write a program to determine if it's possible to reach the target
# position from the starting position within k moves.
# Example:
# n = 3, m = 3
# grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
# start = (0, 0)
# target = (2, 2)
# k = 6
# Output: true

from collections import deque


def is_reachable(n, m, grid, start, target, k):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left

    def is_valid_move(x, y):
        return n > x >= 0 == grid[x][y] and 0 <= y < m

    visited = set()

    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
    visited.add((start[0], start[1]))

    while queue:
        x, y, moves = queue.popleft()

        if (x, y) == target:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid_move(nx, ny) and (nx, ny) not in visited and moves + 1 <= k:
                queue.append((nx, ny, moves + 1))
                visited.add((nx, ny))

    return False
