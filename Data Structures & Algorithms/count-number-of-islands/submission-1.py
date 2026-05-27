class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        directions = ([-1,0],[1,0],[0,-1],[0,1])
        def helper(r,c):
            grid[r][c] = "0"
            for dr,dc in directions:
                neighbor_row = r + dr
                neighbor_col = c + dc
                if 0 <= neighbor_col < cols and 0 <= neighbor_row < rows:
                    if grid[neighbor_row][neighbor_col] == "1":
                        helper(neighbor_row,neighbor_col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count+=1
                    helper(r,c)
        return island_count
