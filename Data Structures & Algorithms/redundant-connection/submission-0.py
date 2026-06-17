class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range((len(edges)+1)))
        print(parents)
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            else:
                parents[py] = px
                return True
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for u,v in edges:
            if union(u,v) == False:
                return [u,v]