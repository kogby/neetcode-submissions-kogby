class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parents = [i for i in range(n)]

        def find(i):
            if parents[i] == i:
                return i

            parents[i] = find(parents[i])
            return parents[i]
        
        for s,e in edges:
            root_s = find(s)
            root_e = find(e)
            if root_s == root_e:
                return False
            parents[root_e] = root_s
        return True

