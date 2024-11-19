class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list for the graph representation
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        # Arrays to track visited nodes and nodes currently in the recursion stack
        visited = [0] * numCourses
        recursionStack = [0] * numCourses

        # Helper function for DFS
        def dfs(course):
            if recursionStack[course]:  # Cycle detected
                return False
            if visited[course]:  # Already visited and no cycle found earlier
                return True

            # Mark the current node as visited and add to the recursion stack
            visited[course] = 1
            recursionStack[course] = 1

            # Visit all the adjacent nodes
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Remove the current node from the recursion stack
            recursionStack[course] = 0
            return True

        # Check for a cycle in each course
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False

        return True