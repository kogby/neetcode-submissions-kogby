class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rottens = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rottens.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        # BFS
        minute = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while rottens and fresh > 0:
            minute += 1
            next_rottens = []
            for x,y in rottens:
                for step_x,step_y in directions:
                    nx, ny = x + step_x, y + step_y
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        next_rottens.append((nx, ny))
            rottens = next_rottens
        
        if fresh != 0:
            return -1
        return minute
            
