class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #put prerequs into an adjacency list
        #run dfs on courses 0 -> numCourses - 1

        #dfs will 1. make sure all courses can be completed and 2. make sure no loops
        graph = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        visited = set()
        def dfs(course: int) -> None:
            if course in visited:
                return False
            if graph[course] == []:
                return True
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            graph[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
