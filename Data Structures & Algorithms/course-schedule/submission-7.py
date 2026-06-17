class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses   # indegree
        graph = [[] for _ in range(numCourses)] # edges

        for u, v in prerequisites:           # v → u
            graph[v].append(u)
            indegree[u] += 1

        no_req = deque(i for i in range(numCourses) if indegree[i] == 0)
        finished = 0

        while no_req:
            node = no_req.popleft()
            finished += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    no_req.append(nei)

        return finished == numCourses 
