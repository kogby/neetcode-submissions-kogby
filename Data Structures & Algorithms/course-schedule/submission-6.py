class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses          # 直接用 array，index 就是節點
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:           # v → u（修完v才能修u）
            graph[v].append(u)
            indegree[u] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        finished = 0

        while queue:
            node = queue.popleft()
            finished += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return finished == numCourses 
