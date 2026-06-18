class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        parents = list(range(n))
        ranks = [0] * n
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x,y):
            rx, ry = find(x), find(y)
            if ranks[rx] < ranks[ry]:
                rx,ry= ry,rx
            if rx!=ry:
                parents[ry] = rx
                return True
            else:
                return False


        for u,v in edges:
            if union(u,v):
                count -=1 

        return count
            