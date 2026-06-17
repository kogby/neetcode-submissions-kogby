class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range((len(edges)+1)))
        ranks = [0] * (len(edges)+1)
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            else:
                if ranks[px] < ranks[py]:
                    px, py = py, px
                parents[py] = px
                if ranks[px] == ranks[py]:
                    ranks[px] += 1
                return True
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for u,v in edges:
            if union(u,v) == False:
                return [u,v]