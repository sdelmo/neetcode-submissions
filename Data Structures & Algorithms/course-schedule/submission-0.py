class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # This is a cycle detection problem
        # Input is given as pairs of (prereq, course)
        # We can convert this into an adjacency list to model the problem
        # such that course: [prereq1, prereq2, etc]

        # Create an adj. list
        adj_list = {i: [] for i in range(numCourses)}
        # Populate it
        for pre, crs in prerequisites:
            adj_list[crs].append(pre)
        
        # Keep set to track visited nodes in DFS path
        visiting = set()

        def dfs(crs):
            # Already visited node in current path, CYCLE
            if crs in visiting:
                return False
            # If course has been tagged as completable
            if adj_list[crs] == []:
                return True
            
            # tag node as visited in dfs path
            visiting.add(crs)
            # visit neighbours, check if they can be completed
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            # remove course from path since it's completable
            visiting.remove(crs)
            # tag as completable
            adj_list[crs] = []
            return True
        
        # Iterate over courses, see if they can all be completed
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
