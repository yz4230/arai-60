class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set[tuple[int, int]]()
        areas = dict[tuple[int, int], int]()
        height, width = len(grid), len(grid[0])

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    continue
                if (row, col) in visited:
                    continue
                stack = list[tuple[int, int]]()
                stack.append((row, col))
                while len(stack) > 0:
                    r, c = stack.pop()
                    if not (0 <= r < height and 0 <= c < width):
                        continue
                    if grid[r][c] == 0:
                        continue
                    if (r, c) in visited:
                        continue
                    visited.add((r, c))
                    areas[(row, col)] = areas.get((row, col), 0) + 1
                    stack.append((r + 1, c))
                    stack.append((r - 1, c))
                    stack.append((r, c + 1))
                    stack.append((r, c - 1))

        if len(areas) > 0:
            return max(areas.values())
        return 0
