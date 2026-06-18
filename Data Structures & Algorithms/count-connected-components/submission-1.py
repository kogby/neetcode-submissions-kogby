class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x,y):
            rx, ry = find(x), find(y)
            parents[ry] = rx

        
        parents = list(range(n))
        for u,v in edges:
            union(u,v)
        for i in range(n):
            parents[i] = find(parents[i])
        print(parents)
        return len(set(parents))
            