class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def DFS(x,y):
            # mark as visited
            board[x][y] = 'V'

            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                    DFS(nx, ny)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        DFS(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X' 
                if board[i][j] == 'V':
                    board[i][j] = 'O' 