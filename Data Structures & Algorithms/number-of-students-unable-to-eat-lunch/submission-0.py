from collections import Counter, deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_count = Counter(students)
        
        i = 0
        while i < len(sandwiches) and stud_count[sandwiches[i]] > 0:
            stud_count[sandwiches[i]] -= 1
            i += 1
            
        return stud_count[0] + stud_count[1]
            




