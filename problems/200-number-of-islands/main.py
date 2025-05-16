class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        height, width = len(grid), len(grid[0])
        visited = [[False for _ in range(width)] for _ in range(height)]
        islands = set[tuple[int, int]]()
        for row in range(height):
            for col in range(width):
                stack = list[tuple[int, int]]()
                if (row, col) in visited:
                    continue
                stack.append((row, col))
                while len(stack) > 0:
                    r, c = stack.pop()
                    if not (0 <= r < height and 0 <= c < width):
                        continue
                    if visited[r][c]:
                        continue
                    visited[r][c] = True
                    if grid[r][c] == "1":
                        islands.add((row, col))
                        stack.append((r + 1, c))
                        stack.append((r - 1, c))
                        stack.append((r, c + 1))
                        stack.append((r, c - 1))

        return len(islands)
