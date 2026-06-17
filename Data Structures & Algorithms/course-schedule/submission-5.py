class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a -> b : (b, a)
        D = {} # degress
        E = {} # edges
        
        for u,v in prerequisites:
            if u not in D:
                D[u] = 1
            else:
                D[u] += 1
            if v not in D:
                D[v] = 0
            if v not in E:
                E[v] = [u]
            else:
                E[v].append(u)
            if u not in E:
                E[u] = []
        # Start with 0 in-degrees
        no_requirements = deque()
        for k, _ in D.items():
            if D[k] == 0:
                no_requirements.append(k)
        
        while len(no_requirements) != 0:
            take = no_requirements.popleft()
            for related_course in E[take]:
                D[related_course] -= 1
                if D[related_course] == 0:
                    no_requirements.append(related_course)

        for k,_ in D.items():
            if D[k] != 0:
                return False
        return True
