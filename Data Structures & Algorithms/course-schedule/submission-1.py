from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = defaultdict(list)
        for [ai, bi] in prerequisites:
            cache[ai].append(bi)
        
        visiting = set()
        visited = set()

        def dfs(course: int):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)
            
            for prereq in cache[course]:
                if not dfs(prereq): 
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course): 
                return False

        return True
