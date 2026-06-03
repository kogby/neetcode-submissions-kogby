class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottens.append((i,j))
        
        # BFS
        minute = -1
        while rottens:
            minute += 1
            next_rottens = []
            for x,y in rottens:
                for step_x,step_y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0 <= x + step_x < len(grid) and 0 <= y + step_y < len(grid[0]) and grid[x + step_x][y + step_y] == 1:
                        grid[x + step_x][y + step_y] = 2
                        next_rottens.append((x+step_x, y+step_y))
            rottens = next_rottens
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        if minute == -1:
            return 0
        return minute
            
