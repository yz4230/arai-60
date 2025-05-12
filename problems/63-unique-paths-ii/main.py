class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        height, width = len(obstacleGrid), len(obstacleGrid[0])

        grid = [[0 for _ in range(width)] for _ in range(height)]
        grid[0][0] = abs(obstacleGrid[0][0] - 1)

        row, col = 0, 0
        while col < width:
            r, c = row, col
            while r >= 0 and c < width:
                if obstacleGrid[r][c] == 0:
                    if r >= 1:
                        grid[r][c] += grid[r - 1][c]
                    if c >= 1:
                        grid[r][c] += grid[r][c - 1]
                r, c = r - 1, c + 1
            if row < height - 1:
                row += 1
            else:
                col += 1

        return grid[-1][-1]


print(
    Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
)
