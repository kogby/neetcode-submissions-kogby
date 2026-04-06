class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_len = len(grid)
        y_len = len(grid[0])
        island_count = 0
    
        def dfs(grid,x,y):
            grid[x][y] = '0'
            next_list = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for next_cord in next_list:
                x_n, y_n = next_cord
                if 0 <= x_n < x_len and 0 <= y_n < y_len:
                    if grid[x_n][y_n] == '1':
                        dfs(grid,x_n,y_n)

        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == '1':
                    island_count += 1
                    dfs(grid,x,y)
        
        return island_count


