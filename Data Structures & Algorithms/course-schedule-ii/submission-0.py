class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            inDegree[u] += 1
            graph[v].append(u) 

        no_req = deque(i for i in range(numCourses) if inDegree[i] == 0)
        finished = []

        while len(no_req) != 0:
            take = no_req.popleft()
            finished.append(take)
            for c in graph[take]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    no_req.append(c)
        if len(finished) == numCourses:
            return finished
        else:
            return []