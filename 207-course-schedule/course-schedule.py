class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        s1=0
        s2=1
        s3=2
        states=[s1]*numCourses
        def dfs(i):
            state=states[i]
            if state==s3:
                return True
            elif state==s2:
                return False
            states[i]=s2
            for n in graph[i]:
                if not dfs(n):
                    return False
            states[i]=s3
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
