class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def DFS(x, y, ocean):
            if (x, y) in ocean:  # ← 加這行避免重複 visit
                return
            ocean.add((x,y))
            cur_height = heights[x][y]
            for next_x, next_y in [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= next_x < len(heights) and 0 <= next_y < len(heights[0]):
                    if cur_height <= heights[next_x][next_y]:
                        DFS(next_x, next_y, ocean)
        
        pacific = set()
        atlantic = set()

        for x in range(len(heights)):
            DFS(x,0,pacific)
            DFS(x,len(heights[0])-1, atlantic)
        for y in range(len(heights[0])):
            DFS(0,y,pacific)
            DFS(len(heights)-1, y, atlantic)

        return [[x, y] for x, y in pacific & atlantic]