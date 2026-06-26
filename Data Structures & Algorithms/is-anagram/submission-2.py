class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
            
        t_copy = t
        for letter in s:
            if letter in t_copy:
                t_copy = t_copy.replace(letter, '', 1)
            else:
                return False
        return True
        