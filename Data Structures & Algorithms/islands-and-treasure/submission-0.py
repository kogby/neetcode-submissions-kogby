class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def DFS(cur_x, cur_y, step):
            # visited and changed minimum step to get to (cur_x, cur_y)
            grid[cur_x][cur_y] = step
            # search for possible direction
            for (i,j) in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_x, next_y = cur_x + i, cur_y + j
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] > step + 1:
                    DFS(next_x, next_y, step + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    DFS(i, j, 0)

