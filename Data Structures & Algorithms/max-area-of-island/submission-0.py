class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x_len = len(grid)
        y_len = len(grid[0])
        max_count = 0
    
        def dfs(grid,x,y):
            count = 1
            grid[x][y] = 0
            next_list = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for next_cord in next_list:
                x_n, y_n = next_cord
                if 0 <= x_n < x_len and 0 <= y_n < y_len:
                    if grid[x_n][y_n] == 1:
                        count += dfs(grid, x_n, y_n)
            return count

        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == 1:
                    cur_cnt = dfs(grid,x,y)
                    if cur_cnt > max_count:
                            max_count = cur_cnt
        
        return max_count